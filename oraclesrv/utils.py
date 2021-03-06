
import re

from flask import current_app
import requests
import flask

from oraclesrv.client import client

def get_solr_data(rows, query, fl):
    """

    :param rows:
    :param query:
    :return:
    """
    result = []

    if current_app.config['REQUESTS_CONNECTION_POOL_ENABLED']:
        response = current_app.client.get(
            url=current_app.config['ORACLE_SERVICE_SOLRQUERY_URL'],
            headers={'Authorization': 'Bearer ' + current_app.config['ORACLE_SERVICE_ADSWS_API_TOKEN']},
            params={'fl': fl, 'rows': rows, 'q': query},
            timeout=current_app.config.get('API_TIMEOUT', 60)
        )
    else:
        new_headers = {}
        if flask.has_request_context():
            # Propagate key information from the original request
            new_headers[u'X-Original-Uri'] = flask.request.headers.get(u'X-Original-Uri', u'-')
            new_headers[u'X-Original-Forwarded-For'] = flask.request.headers.get(u'X-Original-Forwarded-For', u'-')
            new_headers[u'X-Forwarded-For'] = flask.request.headers.get(u'X-Forwarded-For', u'-')
            new_headers[u'X-Amzn-Trace-Id'] = flask.request.headers.get(u'X-Amzn-Trace-Id', '-')
        new_headers[u'Authorization'] = 'Bearer ' + current_app.config['ORACLE_SERVICE_ADSWS_API_TOKEN'] 
        response = requests.get(
            url=current_app.config['ORACLE_SERVICE_SOLRQUERY_URL'],
            headers=new_headers,
            params={'fl': fl, 'rows': rows, 'q': query},
            timeout=current_app.config.get('API_TIMEOUT', 60)
        )


    
    response.raise_for_status()

    from_solr = response.json()
    num_docs = from_solr['response'].get('numFound', 0)
    if num_docs > 0:
        current_app.logger.debug('Got {num_docs} records from solr.'.format(num_docs=num_docs))
        for doc in from_solr['response']['docs']:
            if fl == 'bibcode':
                result.append(doc['bibcode'])
            else:
                result.append(doc)
        return result, response.status_code
    return result, response.status_code

def get_solr_data_recommend(function, reader, rows=5, sort='entry_date', cutoff_days=5, top_n_reads=10):
    """

    :param reader:
    :param rows:
    :param sort:
    :param cutoff_days:
    :param top_n_reads:
    :return:
    """
    query = '({function}(topn({topn}, reader:{reader}, {sort} desc)) entdate:[NOW-{cutoff_days}DAYS TO *])'.format(
               function=function, topn=top_n_reads, reader=reader, sort=sort, cutoff_days=cutoff_days)

    try:
        result, status_code = get_solr_data(rows, query, fl='bibcode')
    except requests.exceptions.HTTPError as e:
        current_app.logger.error(e)
        result = {'error from solr':'%d: %s'%(e.response.status_code, e.response.reason)}
        status_code = e.response.status_code
    return result, query, status_code


re_hyphenated_word = re.compile(r'\w+\-\w+\s*')
re_punctuation = re.compile(r'[^\w\s]')
def get_solr_data_match(abstract, title, doctype, extra_filter):
    """

    :param abstract:
    :param title:
    :param doctype:
    :param extra_filter:
    :return:
    """
    rows = 10
    # if there is an abstract, query solr on abstract, otherwise query on title
    if len(abstract) > 0  and not abstract.lower().startswith('not available'):
        # there is a limit on number of characters that can be send
        abstract = abstract[:2500]
        query = 'topn({rows}, similar("{abstract}", input abstract, {number_matched_terms_abstract}, 1, 1)) doctype:({doctype}) {extra_filter}'.format(rows=rows,
                          abstract=abstract, number_matched_terms_abstract=max(1, int(abstract.count(' ') * 0.3)), doctype=doctype, extra_filter=extra_filter)
    elif len(title) > 0:
        title = re_punctuation.sub('', re_hyphenated_word.sub('', title)).strip()
        query = 'topn({rows}, similar("{title}", input title, {number_matched_terms_title}, 1, 1)) doctype:({doctype}) {extra_filter}'.format(rows=rows,
                          title=title, number_matched_terms_title=max(1, int(title.count(' ') * 0.9)), doctype=doctype, extra_filter=extra_filter)
    else:
        return [], '', 200

    try:
        result, status_code = get_solr_data(rows, query, fl='bibcode,abstract,title,author_norm,year,doctype,identifier')
    except requests.exceptions.HTTPError as e:
        current_app.logger.error(e)
        result = {'error from solr':'%d: %s'%(e.response.status_code, e.response.reason)}
        status_code = e.response.status_code

    return result, query, status_code

def get_solr_data_match_doi(doi, doctype):
    """

    :param doi:
    :param doctype:
    :return:
    """
    try:
        query = 'doi:{doi} doctype:({doctype}) property:REFEREED'.format(doi=doi.replace('(','\(').replace(')','\)'), doctype=doctype)
        result, status_code = get_solr_data(rows=1, query=query, fl='bibcode,doi,abstract,title,author_norm,year,doctype,identifier')
    except requests.exceptions.HTTPError as e:
        current_app.logger.error(e)
        result = {'error from solr':'%d: %s'%(e.response.status_code, e.response.reason)}
        status_code = e.response.status_code

    return result, query, status_code

def get_solr_data_match_thesis(author, year, doctype):
    """

    :param author:
    :param year:
    :return:
    """
    try:
        author = author.split(',')
        author_norm = '{}, {}'.format(author[0].strip(), author[1].strip()[0]).lower()
        query = 'author_norm:"{author}" year:[* TO {year}] doctype:({doctype})'.format(author=author_norm, year=year, doctype=doctype)
        result, status_code = get_solr_data(rows=3, query=query, fl='bibcode,doi,abstract,title,author_norm,year,doctype,identifier')
    except requests.exceptions.HTTPError as e:
        current_app.logger.error(e)
        result = {'error from solr': '%d: %s' % (e.response.status_code, e.response.reason)}
        status_code = e.response.status_code

    return result, query, status_code

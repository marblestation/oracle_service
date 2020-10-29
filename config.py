
# configuration for accessing solr db
# these values can be overwritten by local_config values
ORACLE_SERVICE_SOLRQUERY_URL = "https://dev.adsabs.harvard.edu/v1/search/query"
ORACLE_SERVICE_ADSWS_API_TOKEN = 'this is a secret api token!'

# This is a URL to adsws account info service
ORACLE_SERVICE_ACCOUNT_INFO_URL = '/account/info'

# unicode
ORACLE_SERVICE_UNICODE_CONVERSION = {
    '32': 'blank',
    '33': 'excl',
    '34': 'quot',
    '35': 'num',
    '36': 'dollar',
    '37': 'percent',
    '38': 'amp',
    '39': 'apos',
    '40': 'lpar',
    '41': 'parr0',
    '42': 'ast',
    '43': 'plus',
    '44': 'comma',
    '45': 'hyphen',
    '46': 'period',
    '47': 'sol',
    '58': 'colon',
    '59': 'semi',
    '60': 'lt',
    '61': 'equals',
    '62': 'gt',
    '63': 'quest',
    '64': 'commat',
    '91': 'lsqb',
    '92': 'bsol',
    '93': 'rsqb',
    '95': 'lowbar',
    '105': 'i',
    '123': 'cubl0',
    '124': 'vbm0',
    '125': 'cubr0',
    '160': 'nbsp',
    '161': 'iexcl',
    '162': 'cent',
    '163': 'pound',
    '164': 'curren',
    '165': 'yen',
    '166': 'brvbar',
    '167': 'sect',
    '168': 'Dot',
    '169': 'copy',
    '170': 'ordf',
    '171': 'laquo',
    '172': 'not',
    '173': 'shy',
    '174': 'reg',
    '175': 'macr',
    '176': 'deg',
    '177': 'plusmn',
    '178': 'sup2',
    '179': 'sup3',
    '180': 'acute',
    '181': 'micro',
    '182': 'para',
    '183': 'middot',
    '184': 'cedil',
    '185': 'sup1',
    '186': 'ordm',
    '187': 'raquo',
    '188': 'frac14',
    '189': 'frac12',
    '190': 'frac34',
    '191': 'iquest',
    '192': 'Agrave',
    '193': 'Aacute',
    '194': 'Acirc',
    '195': 'Atilde',
    '196': 'Auml',
    '197': 'Aring',
    '198': 'AElig',
    '199': 'Ccedil',
    '200': 'Egrave',
    '201': 'Eacute',
    '202': 'Ecirc',
    '203': 'Euml',
    '204': 'Igrave',
    '205': 'Iacute',
    '206': 'Icirc',
    '207': 'Iuml',
    '208': 'ETH',
    '209': 'Ntilde',
    '210': 'Ograve',
    '211': 'Oacute',
    '212': 'Ocirc',
    '213': 'Otilde',
    '214': 'Ouml',
    '215': 'times',
    '216': 'Oslash',
    '217': 'Ugrave',
    '218': 'Uacute',
    '219': 'Ucirc',
    '220': 'Uuml',
    '221': 'Yacute',
    '222': 'THORN',
    '223': 'szlig',
    '224': 'agrave',
    '225': 'aacute',
    '226': 'acirc',
    '227': 'atilde',
    '228': 'auml',
    '229': 'aring',
    '230': 'aelig',
    '231': 'ccedil',
    '232': 'egrave',
    '233': 'eacute',
    '234': 'ecirc',
    '235': 'euml',
    '236': 'igrave',
    '237': 'iacute',
    '238': 'icirc',
    '239': 'yicy',
    '240': 'eth',
    '241': 'ntilde',
    '242': 'ograve',
    '243': 'oacute',
    '244': 'ocirc',
    '245': 'otilde',
    '246': 'ouml',
    '247': 'divide',
    '248': 'oslash',
    '249': 'ugrave',
    '250': 'uacute',
    '251': 'ucirc',
    '252': 'uuml',
    '253': 'yacute',
    '254': 'thorn',
    '255': 'yuml',
    '256': 'Amacr',
    '257': 'amacr',
    '258': 'Abreve',
    '259': 'abreve',
    '260': 'Aogon',
    '261': 'aogon',
    '262': 'Cacute',
    '263': 'cacute',
    '264': 'Ccirc',
    '265': 'ccirc',
    '266': 'Cdot',
    '267': 'cdot',
    '268': 'Ccaron',
    '269': 'ccaron',
    '270': 'Dcaron',
    '271': 'dcaron',
    '272': 'Dstrok',
    '273': 'dstrok',
    '274': 'Emacr',
    '275': 'emacr',
    '276': 'Ebreve',
    '277': 'ebreve',
    '278': 'Edot',
    '279': 'edot',
    '280': 'Eogon',
    '281': 'eogon',
    '282': 'Ecaron',
    '283': 'ecaron',
    '284': 'Gcirc',
    '285': 'gcirc',
    '286': 'Gbreve',
    '287': 'gbreve',
    '288': 'Gdot',
    '289': 'gdot',
    '290': 'Gcedil',
    '291': 'gcedil',
    '292': 'Hcirc',
    '293': 'hcirc',
    '294': 'Hstrok',
    '295': 'hstrok',
    '296': 'Itilde',
    '297': 'itilde',
    '298': 'Imacr',
    '299': 'imacr',
    '300': 'Ibreve',
    '301': 'ibreve',
    '302': 'Iogon',
    '303': 'iogon',
    '304': 'Idot',
    '305': 'imath',
    '306': 'IJlig',
    '307': 'ijlig',
    '308': 'Jcirc',
    '309': 'jcirc',
    '310': 'Kcedil',
    '311': 'kcedil',
    '312': 'kgreen',
    '313': 'Lacute',
    '314': 'lacute',
    '315': 'Lcedil',
    '316': 'lcedil',
    '317': 'Lcaron',
    '318': 'lcaron',
    '319': 'Lmidot',
    '320': 'lmidot',
    '321': 'Lstrok',
    '322': 'lstrok',
    '323': 'Nacute',
    '324': 'nacute',
    '325': 'Ncedil',
    '326': 'ncedil',
    '327': 'Ncaron',
    '328': 'ncaron',
    '329': 'napos',
    '330': 'ENG',
    '331': 'eng',
    '332': 'Omacr',
    '333': 'omacr',
    '334': 'Obreve',
    '335': 'obreve',
    '336': 'Odblac',
    '337': 'odblac',
    '338': 'OElig',
    '339': 'oelig',
    '340': 'Racute',
    '341': 'racute',
    '342': 'Rcedil',
    '343': 'rcedil',
    '344': 'Rcaron',
    '345': 'rcaron',
    '346': 'Sacute',
    '347': 'sacute',
    '348': 'Scirc',
    '349': 'scirc',
    '350': 'Scedil',
    '351': 'scedil',
    '352': 'Scaron',
    '353': 'scaron',
    '354': 'Tcedil',
    '355': 'tcedil',
    '356': 'Tcaron',
    '357': 'tcaron',
    '358': 'Tstrok',
    '359': 'tstrok',
    '360': 'Utilde',
    '361': 'utilde',
    '362': 'Umacr',
    '363': 'umacr',
    '364': 'Ubreve',
    '365': 'ubreve',
    '366': 'Uring',
    '367': 'uring',
    '368': 'Udblac',
    '369': 'udblac',
    '370': 'Uogon',
    '371': 'uogon',
    '372': 'Wcirc',
    '373': 'wcirc',
    '374': 'Ycirc',
    '375': 'ycirc',
    '376': 'Yuml',
    '377': 'Zacute',
    '378': 'zacute',
    '379': 'Zdot',
    '380': 'zdot',
    '381': 'Zcaron',
    '382': 'zcaron',
    '402': 'fnof',
    '461': 'Acaron',
    '462': 'acaron',
    '463': 'Icaron',
    '464': 'icaron',
    '465': 'Ocaron',
    '466': 'ocaron',
    '467': 'Ucaron',
    '468': 'ucaron',
    '486': 'Gcaron',
    '487': 'gcaron',
    '488': 'Kcaron',
    '489': 'kcaron',
    '490': 'Oogon',
    '491': 'oogon',
    '496': 'jcaron',
    '500': 'Gacute',
    '501': 'gacute',
    '504': 'Ngrave',
    '505': 'ngrave',
    '537': 'scedil',
    '542': 'Hcaron',
    '543': 'hcaron',
    '550': 'Adot',
    '551': 'adot',
    '552': 'Ecedil',
    '553': 'ecedil',
    '558': 'Odot',
    '559': 'odot',
    '562': 'Ymacr',
    '563': 'ymacr',
    '603': 'epsi',
    '604': 'backeps',
    '607': 'jnodot',
    '699': 'acute',
    '700': 'acute',
    '711': 'caron',
    '729': 'dot',
    '730': 'ring',
    '731': 'ogon',
    '732': 'sim',
    '733': 'dblac',
    '768': 'd13',
    '769': 'acute',
    '770': 'circ',
    '771': 'd5',
    '772': 'd1',
    '774': 'breve',
    '775': 'd2',
    '776': 'd3',
    '780': 'caron',
    '803': 'dotbelow',
    '807': 'cedil',
    '817': 'barbelow',
    '824': 'solidus',
    '913': 'Acy',
    '914': 'Bgr',
    '915': 'Ggr',
    '916': 'Dgr',
    '917': 'Egr',
    '918': 'Zgr',
    '919': 'EEgr',
    '920': 'THgr',
    '921': 'Igr',
    '922': 'Kgr',
    '923': 'Lgr',
    '924': 'Mcy',
    '925': 'Ngr',
    '926': 'Xgr',
    '927': 'Ogr',
    '928': 'Pgr',
    '929': 'Rgr',
    '931': 'Scy',
    '932': 'Tgr',
    '933': 'Ugr',
    '934': 'PHgr',
    '935': 'KHgr',
    '936': 'PSgr',
    '937': 'OHgr',
    '945': 'agr',
    '946': 'bgr',
    '947': 'ggr',
    '948': 'dcy',
    '949': 'ecy',
    '950': 'zgr',
    '951': 'eegr',
    '952': 'thetas',
    '953': 'icy',
    '954': 'kcy',
    '955': 'lgr',
    '956': 'mgr',
    '957': 'ngr',
    '958': 'xgr',
    '959': 'ogr',
    '960': 'pgr',
    '961': 'rgr',
    '962': 'sfgr',
    '963': 'scy',
    '964': 'tgr',
    '965': 'ugr',
    '966': 'phgr',
    '967': 'khcy',
    '968': 'pscy',
    '969': 'ohcy',
    '977': 'thetav',
    '978': 'upsih',
    '981': 'phiv',
    '982': 'piv',
    '988': 'gammad',
    '1008': 'kappav',
    '1009': 'rhov',
    '1013': 'epsilon',
    '1523': 'lsquo',
    '1489': 'beth',
    '1490': 'gimel',
    '1491': 'daleth',
    '7682': 'Bdot',
    '7683': 'bdot',
    '7690': 'Ddot',
    '7691': 'ddot',
    '7696': 'Dcedil',
    '7697': 'dcedil',
    '7710': 'Fdot',
    '7711': 'fdot',
    '7712': 'Gmacr',
    '7713': 'gmacr',
    '7714': 'Hdot',
    '7715': 'hdot',
    '7719': 'huml',
    '7720': 'Hcedil',
    '7721': 'hcedil',
    '7728': 'Kacute',
    '7729': 'kacute',
    '7742': 'Macute',
    '7743': 'macute',
    '7744': 'Mdot',
    '7745': 'mdot',
    '7748': 'Ndot',
    '7749': 'ndot',
    '7764': 'Pacute',
    '7765': 'pacute',
    '7766': 'Pdot',
    '7767': 'pdot',
    '7768': 'Rdot',
    '7769': 'rdot',
    '7776': 'Sdot',
    '7777': 'sdot',
    '7786': 'Tdot',
    '7787': 'tdot',
    '7804': 'Vtilde',
    '7805': 'vtilde',
    '7808': 'Wgrave',
    '7809': 'wgrave',
    '7810': 'Wacute',
    '7811': 'wacute',
    '7814': 'Wdot',
    '7815': 'wdot',
    '7818': 'Xdot',
    '7819': 'xdot',
    '7822': 'Ydot',
    '7823': 'ydot',
    '7824': 'Zcirc',
    '7825': 'zcirc',
    '7868': 'Etilde',
    '7869': 'etilde',
    '7922': 'Ygrave',
    '7923': 'ygrave',
    '7928': 'Ytilde',
    '7929': 'ytilde',
    '8160': 'ubrcy',
    '8168': 'Upsilon',
    '8194': 'ensp',
    '8195': 'emsp',
    '8196': 'emsp13',
    '8197': 'emsp14',
    '8199': 'numsp',
    '8200': 'puncsp',
    '8201': 'ThinSpace',
    '8202': 'hairsp',
    '8208': 'hyphen',
    '8209': 'minus',
    '8210': 'dash',
    '8211': 'ndash',
    '8212': 'mdash',
    '8213': 'horbar',
    '8214': 'dvbm0',
    '8216': 'lsquor',
    '8217': 'rsquor',
    '8220': 'ldquo',
    '8221': 'rdquo',
    '8224': 'dagger',
    '8225': 'Dagger',
    '8226': 'bullet',
    '8229': 'nldr',
    '8230': 'hellip',
    '8231': 'prime',
    '8240': 'permil',
    '8242': 'feet',
    '8243': 'arcsec',
    '8244': 'tprime',
    '8245': 'bprime',
    '8248': 'caret',
    '8249': 'slaquo',
    '8250': 'sraquo',
    '8259': 'hybull',
    '8270': 'ast',
    '8289': 'func',
    '8315': 'minus',
    '8364': 'euro',
    '8407': 'ar',
    '8453': 'incare',
    '8460': 'hamilt',
    '8462': 'plank',
    '8463': 'hslash',
    '8465': 'Im',
    '8466': 'lagran',
    '8467': 'ell',
    '8472': 'weierp',
    '8476': 'Re',
    '8477': 'R',
    '8478': 'rx',
    '8482': 'trade',
    '8484': 'Z',
    '8487': 'mho',
    '8491': 'angst',
    '8492': 'bernou',
    '8499': 'phmmat',
    '8501': 'aleph',
    '8531': 'frac13',
    '8532': 'frac23',
    '8533': 'frac15',
    '8534': 'frac25',
    '8535': 'frac35',
    '8536': 'frac45',
    '8537': 'frac16',
    '8538': 'frac56',
    '8539': 'frac18',
    '8540': 'frac38',
    '8541': 'frac58',
    '8542': 'frac78',
    '8592': 'larr',
    '8593': 'uarr',
    '8594': 'rarr',
    '8595': 'darr',
    '8596': 'harr',
    '8597': 'varr',
    '8598': 'nwarr',
    '8599': 'nearr',
    '8600': 'drarr',
    '8601': 'dlarr',
    '8602': 'nlarr',
    '8603': 'nrarr',
    '8606': 'Larr',
    '8608': 'Rarr',
    '8610': 'larrtl',
    '8611': 'rarrtl',
    '8614': 'map',
    '8617': 'larrhk',
    '8618': 'rarrhk',
    '8619': 'larrlp',
    '8620': 'rarrlp',
    '8621': 'harrw',
    '8622': 'nharr',
    '8624': 'lsh',
    '8625': 'rsh',
    '8630': 'cularr',
    '8631': 'curarr',
    '8634': 'olarr',
    '8635': 'orarr',
    '8636': 'lharu',
    '8637': 'lhard',
    '8638': 'uharr',
    '8639': 'uharl',
    '8640': 'rharu',
    '8641': 'rhard',
    '8642': 'dharr',
    '8643': 'dharl',
    '8644': 'rlarr2',
    '8646': 'lrarr2',
    '8647': 'larr2',
    '8648': 'uarr2',
    '8649': 'rarr2',
    '8650': 'darr2',
    '8651': 'lrhar2',
    '8652': 'rlhar2',
    '8653': 'nlArr',
    '8654': 'nhArr',
    '8655': 'nrArr',
    '8656': 'lArr',
    '8657': 'uArr',
    '8658': 'rArr',
    '8659': 'dArr',
    '8660': 'hArr',
    '8661': 'vArr',
    '8666': 'lAarr',
    '8667': 'rAarr',
    '8669': 'rarrw',
    '8704': 'forall',
    '8705': 'comp',
    '8706': 'part',
    '8707': 'exist',
    '8708': 'nexist',
    '8709': 'Empty',
    '8710': 'Delta',
    '8711': 'nabla',
    '8712': 'isin',
    '8713': 'notin',
    '8714': 'epsilon',
    '8715': 'ni',
    '8719': 'prod',
    '8720': 'coprod',
    '8721': 'sum',
    '8722': 'minus',
    '8723': 'mp',
    '8724': 'plusdo',
    '8725': 'sol',
    '8726': 'setmn',
    '8727': 'lowast',
    '8728': 'cir',
    '8729': 'bull',
    '8730': 'radic',
    '8733': 'prop',
    '8734': 'inf',
    '8735': 'ang90',
    '8736': 'ang',
    '8737': 'angmsd',
    '8738': 'angsph',
    '8739': 'mid',
    '8740': 'nmid',
    '8741': 'Verbar',
    '8742': 'npar',
    '8743': 'and',
    '8744': 'or',
    '8745': 'cap',
    '8746': 'cup',
    '8747': 'int',
    '8750': 'conint',
    '8756': 'there4',
    '8757': 'becaus',
    '8758': 'ratio',
    '8764': 'sim',
    '8765': 'bsim',
    '8768': 'm22',
    '8769': 'nsim',
    '8770': 'eqsim',
    '8771': 'simeq',
    '8772': 'nsime',
    '8773': 'Congruent',
    '8775': 'ncong',
    '8776': 'approx',
    '8777': 'napprox',
    '8778': 'ape',
    '8780': 'bcong',
    '8781': 'asymp',
    '8782': 'bump',
    '8783': 'bumpe',
    '8784': 'esdot',
    '8785': 'eDot',
    '8786': 'efDot',
    '8787': 'erDot',
    '8788': 'colone',
    '8789': 'ecolon',
    '8790': 'ecir',
    '8791': 'circe',
    '8793': 'wedgeq',
    '8796': 'trie',
    '8800': 'neq',
    '8801': 'equiv',
    '8802': 'nequiv',
    '8804': 'leq',
    '8805': 'geq',
    '8806': 'lE',
    '8807': 'gE',
    '8808': 'lnE',
    '8809': 'gnE',
    '8810': 'Lt',
    '8811': 'gg',
    '8812': 'twixt',
    '8814': 'nlt',
    '8815': 'ngt',
    '8816': 'nles',
    '8817': 'nges',
    '8818': 'lsim',
    '8819': 'gsim',
    '8822': 'lg',
    '8823': 'gl',
    '8826': 'pr',
    '8827': 'sc',
    '8828': 'cupre',
    '8829': 'sccue',
    '8830': 'prsim',
    '8831': 'scsim',
    '8832': 'npr',
    '8833': 'nsc',
    '8834': 'sub',
    '8835': 'sup',
    '8836': 'nsub',
    '8837': 'nsup',
    '8838': 'sube',
    '8839': 'supe',
    '8840': 'nsube',
    '8841': 'nsupe',
    '8842': 'vsubne',
    '8843': 'vsupne',
    '8846': 'uplus',
    '8847': 'sqsub',
    '8848': 'sqsup',
    '8849': 'sqsube',
    '8850': 'sqsupe',
    '8851': 'sqcap',
    '8852': 'sqcup',
    '8853': 'oplus',
    '8854': 'ominus',
    '8855': 'otimes',
    '8856': 'osol',
    '8857': 'sun',
    '8858': 'ocir',
    '8859': 'oast',
    '8861': 'odash',
    '8862': 'plusb',
    '8863': 'minusb',
    '8864': 'timesb',
    '8865': 'sdotb',
    '8867': 'dashv',
    '8868': 'top',
    '8869': 'bottom',
    '8870': 'vdash',
    '8871': 'vDash',
    '8872': 'models',
    '8873': 'Vdash',
    '8874': 'Vvdash',
    '8876': 'nvdash',
    '8877': 'nvDash',
    '8878': 'nVdash',
    '8879': 'nVDash',
    '8882': 'vltri',
    '8883': 'vrtri',
    '8884': 'ltrie',
    '8885': 'rtrie',
    '8888': 'mumap',
    '8890': 'intcal',
    '8891': 'veebar',
    '8892': 'barwed',
    '8898': 'cap',
    '8900': 'diam',
    '8901': 'sdot',
    '8902': 'sstarf',
    '8903': 'divonx',
    '8904': 'bowtie',
    '8905': 'ltimes',
    '8906': 'rtimes',
    '8907': 'lthree',
    '8908': 'rthree',
    '8909': 'bsime',
    '8910': 'cuvee',
    '8911': 'cuwed',
    '8912': 'Sub',
    '8913': 'Sup',
    '8914': 'Cap',
    '8915': 'Cup',
    '8916': 'fork',
    '8918': 'ldot',
    '8919': 'gsdot',
    '8920': 'Ll',
    '8921': 'Gg',
    '8922': 'leg',
    '8923': 'gel',
    '8926': 'cuepr',
    '8927': 'cuesc',
    '8928': 'npre',
    '8929': 'nsce',
    '8934': 'lnsim',
    '8935': 'gnsim',
    '8936': 'prnsim',
    '8937': 'scnsim',
    '8938': 'nltri',
    '8939': 'nrtri',
    '8940': 'nltrie',
    '8941': 'nrtrie',
    '8942': 'm7',
    '8943': 'cdots',
    '8944': 'ddots',
    '8966': 'Barwed',
    '8968': 'ceill0',
    '8969': 'ceilr0',
    '8970': 'fll0',
    '8971': 'flr0',
    '8972': 'drcrop',
    '8973': 'dlcrop',
    '8974': 'urcrop',
    '8975': 'ulcrop',
    '8988': 'ulcorn',
    '8989': 'urcorn',
    '8990': 'dlcorn',
    '8991': 'drcorn',
    '8994': 'frown',
    '8995': 'smile',
    '9001': 'angl0',
    '9002': 'angr0',
    '9415': 'circledR',
    '9416': 'circS',
    '9472': 'ndash',
    '9632': 'missing',
    '9633': 'squ',
    '9645': 'rect',
    '9651': 'xutri',
    '9652': 'utrif',
    '9653': 'utri',
    '9656': 'rtrif',
    '9657': 'rtri',
    '9661': 'xdtri',
    '9662': 'dtrif',
    '9663': 'dtri',
    '9666': 'ltrif',
    '9667': 'ltri',
    '9674': 'loz',
    '9711': 'xcirc',
    '9733': 'starf',
    '9737': 'sun',
    '9792': 'female',
    '9793': 'earth',
    '9794': 'male',
    '9824': 'spades',
    '9825': 'hearts',
    '9826': 'diams',
    '9827': 'clubs',
    '9830': 'lozf',
    '9837': 'flat',
    '9838': 'natur',
    '9839': 'sharp',
    '10003': 'check',
    '10016': 'malt',
    '10216': 'mlab',
    '10217': 'mrab',
    '10877': 'les',
    '10878': 'ges',
    '10886': 'gap',
    '10889': 'lap',
}

ORACLE_SERVICE_MATCH_DOCTYPE = {
    'eprint': ['article', 'inproceedings', 'inbook'],
    'article': ['eprint'],
    'inproceedings': ['eprint'],
    'inbook': ['eprint'],
    'thesis': ['phdthesis', 'mastersthesis']
}
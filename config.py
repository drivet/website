YAWT_BASE_URL = 'http://localhost'
YAWT_CONTENT_FOLDER = 'content'
YAWT_DRAFT_FOLDER = 'drafts'
YAWT_TEMPLATE_FOLDER = 'templates'
YAWT_DEFAULT_FLAVOUR = 'html'
YAWT_INDEX_FILE = 'index'
YAWT_ARTICLE_TEMPLATE = 'article'
YAWT_ARTICLE_EXTENSIONS = ['txt']
YAWT_DEFAULT_EXTENSION = 'txt'
YAWT_STATE_FOLDER = '_state'
YAWT_MULTIMARKDOWN_FILE_EXTENSIONS = ['md', 'txt']

from whoosh.fields import TEXT, DATETIME, IDLIST
WHOOSH_INDEX_ROOT = '/home/dcr/blogging/website/_state/index'
YAWT_WHOOSH_ARTICLE_INFO_FIELDS = {'create_time': DATETIME(sortable=True),
                                   'categories': IDLIST()}
YAWT_WHOOSH_ARTICLE_FIELDS = {'content': TEXT()}

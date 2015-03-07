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

YAWT_TAGGING_BASE = '/blog/'
YAWT_TAGGING_COUNT_FILE = 'tagcounts'

YAWT_CATEGORY_BASE = '/blog/'
YAWT_CATEGORY_COUNT_FILE = 'categorycounts'

YAWT_COLLECTIONS_SORT_FIELD = 'smart_create_time'
YAWT_ARCHIVE_DATEFIELD = 'smart_create_time'
YAWT_ARCHIVE_BASE = '/blog/'

from whoosh.fields import TEXT, DATETIME, IDLIST, KEYWORD
WHOOSH_INDEX_ROOT = '/home/dcr/blogging/website/_state/index'
YAWT_WHOOSH_ARTICLE_INFO_FIELDS = {'smart_create_time': DATETIME(sortable=True),
                                   'categories': IDLIST(),
                                   'tags': KEYWORD(commas=True)}
YAWT_WHOOSH_ARTICLE_FIELDS = {'content': TEXT()}

GIT_REPOPATH = '/home/dcr/blogging/website'

YAWT_SMART_ATTRIBUTES = {
    'smart_create_time': ['ctime', 'git_create_time', 'create_time'],
    'smart_modified_time': ['mtime', 'git_modified_time', 'modified_time'],
    'smart_author': ['author', 'git_author']
}

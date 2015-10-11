YAWT_BASE_URL = 'http://www.desmondrivet.com'
YAWT_CONTENT_FOLDER = 'content'
YAWT_DRAFT_FOLDER = 'drafts'
YAWT_TEMPLATE_FOLDER = 'templates'
YAWT_DEFAULT_FLAVOUR = 'html'
YAWT_INDEX_FILE = 'index'
YAWT_ARTICLE_TEMPLATE = 'article'
YAWT_ARTICLE_EXTENSIONS = ['txt']
YAWT_STATE_FOLDER = '_state'
YAWT_CONTENT_TYPE_RSS = 'application/rss+xml'
YAWT_META_TYPES = {'create_time': 'iso8601',
                   'modified_time': 'iso8601',
                   'tags': 'list'}

YAWT_EXTENSIONS = ['yawtext.multimarkdown.YawtMarkdown',
                   'yawtext.excerpt.YawtExcerpt',
                   'yawtext.vc.YawtVersionControl',
                   'yawtext.breadcrumbs.YawtBreadcrumbs',
                   'yawtext.categories.YawtCategories',
                   'yawtext.categories.YawtCategoryCounter',
                   'yawtext.tagging.YawtTagging',
                   'yawtext.tagging.YawtTagCounter',
                   'yawtext.archives.YawtArchives',
                   'yawtext.archives.YawtArchiveCounter',
                   'flask_whoosh.Whoosh',
                   'yawtext.indexer.YawtIndexer',
                   'yawtext.collections.YawtCollections',
                   'yawtext.search.YawtSearch',
                   'yawtext.micropost.YawtMicropost',
                   'yawtext.sync.YawtSync',
                   'yawtext.notify.YawtNotify',
                   'yawtext.autodates.YawtAutodates',
                   'yawtext.autotags.YawtAutotags']

YAWT_EXCERPT_WORDCOUNT = 100

YAWT_MULTIMARKDOWN_FILE_EXTENSIONS = ['md', 'txt']
YAWT_MULTIMARKDOWN_EXTENSIONS = ['extra', 'codehilite', 'tables',
                                 'gfm.autolink:AutolinkExtension']


from whoosh.fields import TEXT, DATETIME, IDLIST, KEYWORD
WHOOSH_INDEX_ROOT = '/home/dcr/blogging/website/_state/index'
YAWT_INDEXER_WHOOSH_INFO_FIELDS = {'create_time': DATETIME(sortable=True),
                                   'categories': IDLIST(),
                                   'tags': KEYWORD()}
YAWT_INDEXER_WHOOSH_FIELDS = {'content': TEXT(vector=True)}


YAWT_COLLECTIONS_SORT_FIELD = 'create_time'

YAWT_TAGGING_BASE = ['blog', 'microposts']
YAWT_TAGGING_COUNT_FILE = 'tagcounts'
YAWT_TAGGING_FULL_ARTICLE_FLAVOURS = ['rss']

YAWT_CATEGORY_BASE = ['blog']
YAWT_CATEGORY_COUNT_FILE = 'categorycounts'
YAWT_CATEGORY_FULL_ARTICLE_FLAVOURS = ['rss']

YAWT_ARCHIVE_DATEFIELD = 'create_time'
YAWT_ARCHIVE_BASE = ['blog', 'microposts']

YAWT_MICROPOST_NETWORKS = ['facebook', 'twitter']
YAWT_NOTIFY_BASE_URL = 'http://www.desmondrivet.com'
YAWT_NOTIFY_CATEGORIES = ['blog']
YAWT_NOTIFY_HOSTS = ['argon']
YAWT_NOTIFY_NETWORKS = ['facebook', 'twitter']

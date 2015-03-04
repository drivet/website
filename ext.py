from yawtext.multimarkdown import YawtMarkdown
from flask_whoosh import Whoosh
from yawtext.indexer import YawtWhoosh
from yawtext.collections import YawtPaging
from yawtext.categories import YawtCategories
from yawtext.excerpt import YawtExcerpt
from yawtext.search import YawtSearch
from yawtext.tagging import YawtTagging
from yawtext.breadcrumbs import YawtBreadcrumbs

yawtmarkdown = YawtMarkdown()
whoosh = Whoosh()
yawtwhoosh = YawtWhoosh()
yawtpaging = YawtPaging()
yawtcategories = YawtCategories()
yawtexcerpt = YawtExcerpt()
yawtsearch = YawtSearch()
yawttagging = YawtTagging()
yawtbreadcrumbs = YawtBreadcrumbs()

def init_app(app):
    yawtmarkdown.init_app(app)
    whoosh.init_app(app)
    yawtwhoosh.init_app(app)
    yawtpaging.init_app(app)
    yawtcategories.init_app(app)
    yawtexcerpt.init_app(app)
    yawtsearch.init_app(app)
    yawttagging.init_app(app)
    yawtbreadcrumbs.init_app(app)

extension_info = [
    {'yawtmarkdown': yawtmarkdown,
     'whoosh': whoosh,
     'yawtwhoosh': yawtwhoosh,
     'yawtpaging': yawtpaging, 
     'yawtcategories': yawtcategories,
     'yawtexcerpt': yawtexcerpt,
     'yawtsearch': yawtsearch,
     'yawttagging': yawttagging,
     'yawtbreadcrumbs': yawtbreadcrumbs,
    },

    [yawtmarkdown, yawtexcerpt, yawtbreadcrumbs, 
     yawtcategories, yawttagging, 
     whoosh, yawtwhoosh, yawtpaging, yawtsearch ],

    init_app
]

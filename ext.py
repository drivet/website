from yawtext.multimarkdown import YawtMarkdown
from flask_whoosh import Whoosh
from yawtext.indexer import YawtWhoosh
from yawtext.collections import YawtPaging
from yawtext.categories import YawtCategories
from yawtext.excerpt import YawtExcerpt
from yawtext.search import YawtSearch

yawtmarkdown = YawtMarkdown()
whoosh = Whoosh()
yawtwhoosh = YawtWhoosh()
yawtpaging = YawtPaging()
yawtcategories = YawtCategories()
yawtexcerpt = YawtExcerpt()
yawtsearch = YawtSearch()

def init_app(app):
    yawtmarkdown.init_app(app)
    whoosh.init_app(app)
    yawtwhoosh.init_app(app)
    yawtpaging.init_app(app)
    yawtcategories.init_app(app)
    yawtexcerpt.init_app(app)
    yawtsearch.init_app(app)

extension_info = [
    {'yawtmarkdown': yawtmarkdown,
     'whoosh': whoosh,
     'yawtwhoosh': yawtwhoosh,
     'yawtpaging': yawtpaging, 
     'yawtcategories': yawtcategories,
     'yawtexcerpt': yawtexcerpt,
     'yawtsearch': yawtsearch
    },

    [yawtmarkdown, whoosh, yawtwhoosh, yawtpaging, yawtcategories, yawtexcerpt, yawtsearch],

    init_app
]

from yawtext.multimarkdown import YawtMarkdown
from flask_whoosh import Whoosh
from yawtext.indexer import YawtWhoosh
from yawtext.collections import YawtPaging
from yawtext.categories import YawtCategories
from yawtext.categorycounts import YawtCategoryCount
from yawtext.excerpt import YawtExcerpt
from yawtext.search import YawtSearch
from yawtext.tagging import YawtTagging
from yawtext.tagcount import YawtTagCount

yawtmarkdown = YawtMarkdown()
whoosh = Whoosh()
yawtwhoosh = YawtWhoosh()
yawtpaging = YawtPaging()
yawtcategories = YawtCategories()
yawtcategorycount = YawtCategoryCount()
yawtexcerpt = YawtExcerpt()
yawtsearch = YawtSearch()
yawttagging = YawtTagging()
yawttagcount = YawtTagCount()

def init_app(app):
    yawtmarkdown.init_app(app)
    whoosh.init_app(app)
    yawtwhoosh.init_app(app)
    yawtpaging.init_app(app)
    yawtcategories.init_app(app)
    yawtcategorycount.init_app(app)
    yawtexcerpt.init_app(app)
    yawtsearch.init_app(app)
    yawttagging.init_app(app)
    yawttagcount.init_app(app)

extension_info = [
    {'yawtmarkdown': yawtmarkdown,
     'whoosh': whoosh,
     'yawtwhoosh': yawtwhoosh,
     'yawtpaging': yawtpaging, 
     'yawtcategories': yawtcategories,
     'yawtcategorycount': yawtcategorycount,
     'yawtexcerpt': yawtexcerpt,
     'yawtsearch': yawtsearch,
     'yawttagging': yawttagging,
     'yawttagcount': yawttagcount
    },

    [yawtmarkdown, whoosh, yawtwhoosh, yawtpaging, yawtcategories, 
     yawtcategorycount, yawtexcerpt, yawtsearch, yawttagging, yawttagcount],

    init_app
]

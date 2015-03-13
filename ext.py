from yawtext.multimarkdown import YawtMarkdown
from flask_whoosh import Whoosh
from yawtext.indexer import YawtWhoosh
from yawtext.collections import YawtCollections
from yawtext.categories import YawtCategories
from yawtext.excerpt import YawtExcerpt
from yawtext.search import YawtSearch
from yawtext.tagging import YawtTagging
from yawtext.breadcrumbs import YawtBreadcrumbs
from flask_git import Git
from yawtext.git import YawtGit
from yawtext.smartattributes import YawtSmartAttributes
from yawtext.archives import YawtArchives

yawtmarkdown = YawtMarkdown()
whoosh = Whoosh()
yawtwhoosh = YawtWhoosh()
yawtcollections = YawtCollections()
yawtcategories = YawtCategories()
yawtexcerpt = YawtExcerpt()
yawtsearch = YawtSearch()
yawttagging = YawtTagging()
yawtbreadcrumbs = YawtBreadcrumbs()
git = Git()
yawtgit = YawtGit()
yawtsmart = YawtSmartAttributes()
yawtarchives = YawtArchives()

def init_app(app):
    yawtmarkdown.init_app(app)
    whoosh.init_app(app)
    yawtwhoosh.init_app(app)
    yawtcollections.init_app(app)
    yawtcategories.init_app(app)
    yawtexcerpt.init_app(app)
    yawtsearch.init_app(app)
    yawttagging.init_app(app)
    yawtarchives.init_app(app)
    yawtbreadcrumbs.init_app(app)
    git.init_app(app)
    yawtgit.init_app(app)
    yawtsmart.init_app(app)

extension_info = [
    {'yawtmarkdown': yawtmarkdown,
     'whoosh': whoosh,
     'yawtwhoosh': yawtwhoosh,
     'yawtcollections': yawtcollections,
     'yawtcategories': yawtcategories,
     'yawtexcerpt': yawtexcerpt,
     'yawtsearch': yawtsearch,
     'yawttagging': yawttagging,
     'yawtarchives': yawtarchives,
     'yawtbreadcrumbs': yawtbreadcrumbs,
     'git': git,
     'yawtgit': yawtgit,
     'yawtsmart': yawtsmart
    },

    [yawtexcerpt, yawtmarkdown, git, yawtgit, yawtsmart, yawtbreadcrumbs, 
     yawtcategories, yawttagging, yawtarchives,
     whoosh, yawtwhoosh, yawtcollections, yawtsearch],

    init_app
]

from tasks.meta import OBSTag
from tasks.base_tasks import TagsTask


class NYCTags(TagsTask):

    def version(self):
        return 1

    def tags(self):
        return [
            OBSTag(id='nyc',
                   name="New York City",
                   type='section')
        ]

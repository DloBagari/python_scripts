from post import Post
from collections import defaultdict
import datetime
import json

class Blog:
    def __init__(self, title, post = None):
        self.title = title
        self.entries = post if post is not None else []
        
    def  append(self, post):
        self.entries.append(post)

    def by_tag(self):
        tag_index = defaultdict(list)
        for post in self.entries:
            for tag in post.tags:
                tag_index[tag].append(post.as_dict())
        return tag_index

    def as_dict(self):
        return dict(
            title = self.title,
            underline = "="*len(self.title),
            entries = [p.as_dict() for p in self.entries])

    def _json(self):
        return dict(
            __class__ = self.__class__.__name__,
            __args__ = [self.title, self.entries],
            __kw__ = {})
    


if __name__ == "__main__":
    travel = Blog("Travel")
    travel.append( Post( date = datetime.datetime(2016,6, 14, 1, 31,24),
                            title = "Dlo Bagari",
                            rst_text = " some other text",
                            tags = ("#233AS", "#SDE45S")))
    travel.append( Post( date = datetime.datetime(2016,6, 14, 1, 31,24),
                            title = "Dlo Bagari2",
                            rst_text = " some other text2",
                            tags = ("#455AS6", "#66E4567")))
    #output show how object translated from python to json notation
    print(json.dumps(travel.as_dict(), indent=4))

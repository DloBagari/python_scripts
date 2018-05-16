from collections import defaultdict

class Blog:
    def __init__(self, **kw):
        """requires title"""
        self.id = kw.pop("id", None)
        self.title = kw.pop("title", None)
        if kw:
            raise TooManyValues(kw)
        self.entries = list()

    def append(self, post):
        self.entries.append(post)

    def by_tag(self):
        tags_index = defaultdict(list)
        for post in self.entries:
            for tag in post.tags:
                tags_index[tag].append(post)

        return tags_index

    def as_dict(self):
        return dict(
            title = self.title,
            underline = "=" * len(self.title),
            entries = (p.as_dict() for p in self.entries))


class Post:
    def __init__(self, **kw):
        """requires date, title, rst_text"""
        self.id = kw.pop("id", None)
        self.title = kw.pop("title", None)
        self.date = kw.pop("date", None)
        self.rst_text = kw.pop("rst_text", None)
        self.tags = list()
        if kw:
            raise TooManyValues(kw)

    def append(self, tag):
        self.tags.append(tag)

    def as_dict(self):
        return dict(
            date = str(self.date),
            title = self.title,
            rst_text = self.rst_text,
            underline = "_" * len(self.title),
            tags = " ".join(self.tags))

class TooManyValues(Exception):
    pass


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

    def __str__(self):
        return "{__class__.__name__}(id: {id!r})".format(__class__ = self.__class__,
                                                    id=self._id)
    __repr__= __str__
    

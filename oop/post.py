class Post:
    def __init__(self, date, title, rst_text, tags):
        self.date = date
        self.title = title
        self.rst_text = rst_text
        self.tags = tags

    def as_dict(self):
        return dict(
            date = str(self.date),
            title = self.title,
            underline = "-"*len(self.title),
            rst_text = self.rst_text,
            tag_text = " ".join(self.tags))

    def _json (self):
        return dict(
            __class__ = self.__class__.__name__,
            __args__ = [],
            __kw__ = dict(
                date = self.date,
                title = self.title,
                rst_text = self.rst_text,
                tags = self.tags))
    
    def __str__(self):
        return "{__class__.__name__}(id: {id!r})".format(__class__ = self.__class__,
                                                    id=self._id)
    __repr__= __str__


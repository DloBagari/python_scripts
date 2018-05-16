from access_shelve2 import Access2

class Access3(Access2)ssss:
    def new(self, *args, **kw):
        super().new(*args, **kw)
        self.database["_DB:Blog"] = list()
   

    def add_blog(self, blog):
        blog = super().add_blog(blog)
        blogs = self.database["_DB:Blog"]
        blogs.append(blog._id)
        self.database["_DB:Blog"] = blogs
        return blog

    def blog_iter(self):
        return (self.database[k] for k in self.database["_DB:Blog"])
    

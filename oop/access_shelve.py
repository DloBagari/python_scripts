import shelve
import re


class Access:
    def new(self, filename):
        self.database = shelve.open(filename, "n")
        self.max = {"Blog":0, "Post":0}
        self.sync()

    def open(self, filename):
        self.database = shelve.open(filename, "w")
        self.max = self.database["_DB:max"]

    def close(self):
        if self.database:
            self.database["_DB:max"] = self.max
            self.database.close()
        self.database = None

    def sync(self):
        self.database["_DB:max"] = self.max
        self.database.sync()

    def quit(self):
        self.close()

    def add_blog(self, blog):
        self.max["Blog"] +=1
        key = "Blog:{id}".format(id = self.max["Blog"])
        blog._id = key
        self.database[blog._id] = blog
        return blog

    def get_blog(self, id):
        return self.database[id]

    def add_post(self, blog, post):
        self.max["Post"] +=1
        try:
            key = "{blog}:Post:{id}".format(blog = blog._id, id = self.max["Post"])
        except AttibuteError:
            self.max["Post"] -=1
            raise OperationError("Blog not Added")
        post._id = key
        self.database[post._id] = post
        return post

    def get_post(self, id):
        return self.database[id]

    def replace_post(self, post):
        self,database[post._id] = post
        return post

    def delete_post(self, post):
        del self.database[post._id]

    def __iter__(self):
        for k in self.database:
            if k[0] == "_":
                continue
            yield self.database[k]

    def blog_iter(self):
        for k in self.database:
            if re.match(r"^Blog:\d+$", k):
                yield self.database[k]

    def post_iter(self, blog):
        for k in self.database:
            #here the format will take place first and the the row string will
            #be created
            if re.match(r"^{blog}:Post:\d+$".format(blog=blog._id), k):
                yield self.database[k]

    #iteration on title of the post
    def title_iter(self, blog,title):
        return (p for o in self.post_iter(blog) if p.title == title)
                    
        

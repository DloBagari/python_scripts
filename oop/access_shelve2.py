"""in this class we will increase the perfornamce using index """
from access_shelve import Access
import re
class Access2(Access):
    #override some methods

    def add_blog(self, blog):
        blog = super().add_blog(blog)
        blog._post_list = []
        self.database[blog._id] = blog
        return blog

    def add_post(self, blog, post):
        post = super().add_post(blog, post)
        blog._post_list.append(post._id)
        self.database[blog._id] = blog
        return post

    def delete_post(self, post):
        del self.database[post._id]
        match = re.match(r"(^Blog:\d+):Post:\d+$" ,post._id)
        blog = self.database[match.group(1)]
        blog._post_list.remove(post._id)
        self.database[blog._id] = blog

    #using the feature of blog._post_list we can make post_iter()
    #use indecis not Brute_force search

    def post_iter(self, blog):
        for k in blog._post_list:
            yield self.database[k]
        

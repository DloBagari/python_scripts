from blog import Blog
from post import Post
from contextlib import closing
from access_shelve import Access
import datetime
from access_shelve2 import Access2
from access_shelve3 import Access3

with closing(Access()) as access:
    access.new("blog")
    b1 = Blog("Dlo")
    access.add_blog(b1)
    #id for blog as been set

    p1 = Post(datetime.datetime(2016,6,23,12,34,34), "python",
              "pickle and shelve programming", ("#53H","#45R"))
    access.add_post(b1, p1)
    #id for post is been created and set
    p2 = Post(datetime.datetime(2016,6,23,12,34,34), "Java",
              "javafx programming", ("#89W","#18V"))
    access.add_post(b1,p2)

    b = access.get_blog(b1._id)
    print(b1,b)
    print(b._id)
    for p in access.post_iter(b):
        print(p, p._id)
    access.quit()


with closing(Access2()) as access:
    access.new("blog")
    b1 = Blog("Dlo")
    access.add_blog(b1)
    #id for blog as been set

    p1 = Post(datetime.datetime(2016,6,23,12,34,34), "python",
              "pickle and shelve programming", ("#53H","#45R"))
    access.add_post(b1, p1)
    #id for post is been created and set
    p2 = Post(datetime.datetime(2016,6,23,12,34,34), "Java",
              "javafx programming", ("#89W","#18V"))
    access.add_post(b1,p2)

    b = access.get_blog(b1._id)
    print(b1,b)
    print(b._id)
    for p in access.post_iter(b):
        print(p, p._id)
        access.delete_post(p)
    access.quit()

with closing(Access3()) as access:
    access.new("blog")
    b1 = Blog("Dlo")
    access.add_blog(b1)
    #id for blog as been set

    p1 = Post(datetime.datetime(2016,6,23,12,34,34), "python",
              "pickle and shelve programming", ("#53H","#45R"))
    access.add_post(b1, p1)
    #id for post is been created and set
    p2 = Post(datetime.datetime(2016,6,23,12,34,34), "Java",
              "javafx programming", ("#89W","#18V"))
    access.add_post(b1,p2)

    b = access.blog_iter()
    for i in b:
        for p in access.post_iter(i):
            print(p, p._id)
            access.delete_post(p)
    access.quit() 
    

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table
from sqlalchemy import BigInteger, Boolean, Date, DateTime, Enum,Float,\
     Integer, Interval, Numeric , PickleType, SmallInteger, String, Text, \
     Time, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import sqlalchemy.orm.exc

#metaclass
Base = declarative_base()


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True)
    title = Column(String)

    def as_dict(self):
        return dict(
            title = self.title,
            underline = "=" * len(self.title),
            entries = [ p.as_dict() for p in self.entries]
        )

    def __str__(self):
        return "{__class__.__name__}(title = {title})".format(\
            __class__ = self.__class__, title = self.title)
    __repr__ = __str__


#we did not manage to avoid duplicated Blog or Post
#we have to check if the blog is exit before adding it to session
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(DateTime)
    rst_text = Column(UnicodeText)
    #"blog.id" is the blog which has relationship with this class
    blog_id = Column(Integer, ForeignKey("blog.id"))
    #when any Blog instance is created it will have an attribute entries
    #which will be en empty list
    #this class will be like listener is ve create any Post
    #it will automatically be added to the blog.entries
    #which blog will be add? the blog parameter when we create post instance
    #and post.blog = given blog in parameters
    blog = relationship("Blog", backref="entries")
    #each tag in tags will have attibute posts that is a list
    #creating instance of the post with tags parameter = list to Tag objects
    #will append the post object to each Tag.posts
    tags = relationship("Tag", secondary="assoc_post_tag",
                        backref="posts")

    def as_dict(self):
        return dict(
            title = self.title,
            date = self.date,
            rst_text = self.rst_text,
            underline = "_" * len(self.title),
            tags = [ t.phrase for t in self.tags]
            )

    def __str__(self):
        return "{__class__.__name__}(title = {title})".format(\
            __class__= self.__class__, title = self.title)
    
    def __repr__(self):
        return str(self)

class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    phrase = Column(String, unique=True)


assoc_post_tag = Table("assoc_post_tag", Base.metadata,
                       Column("post_id", ForeignKey("post.id")),
                       Column("tag_id", ForeignKey("tag.id")))

engine = create_engine("sqlite:///./blog_database.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

blog = Blog(title="travel")
session.add(blog)

tags = []
for phrase in "tag1", "tag2", "tag3":
    try:
        tag = session.query(Tag).filter(Tag.phrase == phrase).one()
    except sqlalchemy.orm.exc.NoResultFound:
        tag = Tag(phrase=phrase)
        session.add(tag)
    tags.append(tag)


p2 = Post(date=datetime.datetime(2016, 7, 3, 1,19), title ="dlo",
          rst_text = "some @ test &$",
          blog = blog,
          tags = tags)
session.add(p2)
blog.posts= [p2]
print("\npost.blog",p2.blog)
for tag in tags:
    print(tag.posts)

#commit
session.commit()
print("end session\n\n\n")
#create empty session to read from database not from the exist session chache
session = Session()
for blog in session.query(Blog):
    print(blog)
    for p in blog.entries:
        print(p.as_dict())

#join tables
print("\n\nprinting resylt of join")
for post in session.query(Post).join(assoc_post_tag).join(Tag).filter(\
    Tag.phrase == "tag1"):
    print(post.blog.title, post.date,[t.phrase for t in post.tags])


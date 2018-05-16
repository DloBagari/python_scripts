import sqlite3
from mapping_object_to_sql import *
class Access:
    get_last_id = """
SELECT last_insert_rowid()
"""
    def open(self, filename):
        self.database = sqlite3.connect(filename)
        #row_factory = sqlite3.Row  will set row class instead of a simple tuple
        #the row class allows access via the numeric index as well the column name
        self.database.row_factory = sqlite3.Row

    def get_blog(self, id):
        query = """
        SELECT * FROM blog WHERE id = ?
        """
        query_post = """
        SELECT * FROM post WHERE blog_id = ?
        """
        row = self.database.execute(query, (id,)).fetchone()
        blog = Blog(id=row[0], title=row[1])
        row = self.database.execute(query_post, (id,))
        if row is not None:
            for p in row:
                pos = self.get_post(p[0])
                blog.append(pos)
        
        return blog

    def add_blog(self, blog):
        query="""
         INSERT INTO blog(title) VALUES(:title)
         """
        self.database.execute(query,dict(title=blog.title))
        row = self.database.execute(__class__.get_last_id).fetchone()
        blog.id = row[0]
        for post in blog.entries:
            self.add_post(blog, post)
        return blog

    def build_tables(self, query):
        for q in query.split(";"):
            self.database.execute(q)


    def get_post(self, id):
        query_post = """
        SELECT * FROM post WHERE id = ?
        """
        query_tag = """
        SELECT tags.* FROM tags JOIN assoc_post_tag ON
        tags.id = assoc_post_tag.tag_id WHERE assoc_post_tag.post_id = ?
        """
        row = self.database.execute(query_post, (id,)).fetchone()
        post = Post(id = row["id"], title=row["title"],
                    date=row["date"], rst_text = row["rst_text"])

        tags = self.database.execute(query_tag, (id,))
        for id, tag in tags:
            post.append(tag)
        return post

    def add_post(self, blog, post):
        insert_post = """
        INSERT INTO post(date, title, rst_text, blog_id)
        VALUES(:date, :title, :rst_text, :blog_id)
        """
        query_tag = """
        SELECT * FROM tags WHERE phrase=?
        """
        insert_tag = """
        INSERT INTO tags(phrase) VALUES(?)
        """
        
        insert_assciation = """
        INSERT INTO assoc_post_tag(post_id, tag_id) VALUES(:post_id, :tag_id)
        """
        with self.database:
            self.database.execute(insert_post, dict(date=post.date, title=post.title,
                            rst_text=post.rst_text, blog_id=blog.id))
            row = self.database.execute(__class__.get_last_id).fetchone()
            post.id = row[0]
            for tag in post.tags:
                tag_row = self.database.execute(query_tag, (tag,)).fetchone()
                if tag_row is not None:
                    tag_id = row[0]
                else:
                    self.database.execute(insert_tag, (tag,))
                    row = self.database.execute(__class__.get_last_id).fetchone()
                    tag_id = row[0]
                self.database.execute(insert_assciation,dict(post_id=post.id,
                                                     tag_id =tag_id))
        return post

    def blog_iter(self):
        query = """
        SELECT id FROM blog
        """
        rows = self.database.execute(query)
        for row in rows:
            yield self.get_blog(row[0])
        
        

                                     
    
    

class CreateTables:
    @staticmethod
    def create():
        return """
CREATE TABLE blog(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT);
CREATE TABLE post(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TIMESTAMP,
title TEXT,
rst_text TEXT,
blog_id INTEGER REFERENCES blog(id));
CREATE TABLE tags(
id INTEGER PRIMARY KEY AUTOINCREMENT,
phrase TEXT UNIQUE ON CONFLICT FAIL);
CREATE TABLE assoc_post_tag(
post_id INTEGER REFERENCES post(id),
tag_id INTEGER REFERENCES tag(id))
"""
    

from access_layer_sqlite import *
from mapping_object_to_sql import *
from create_tables import *

s = Access()
s.open("dd.db")
s.build_tables(CreateTables.create())

b = Blog(title = "dlo")

p = Post(title="post1", date="2016",rst_text="some thext")
p.append("tag1")
p.append("tag2")
b.append(p)

s.add_blog(b)
b2 = s.get_blog(1)
result=b2.as_dict()
print(result)
print(list(result["entries"]))
for i in s.blog_iter():
    print("\n\n",i.as_dict())

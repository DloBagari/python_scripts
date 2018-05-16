from json_dumps import Blog
from post import Post
import datetime
import json
import yaml


def blog_encode(object):
    if isinstance(object, datetime.datetime):
        fmt = "%Y-%m-%dT%H:%M:%S"
        return dict(
            __class__ = "datetime.datetime.strptime",
            __args__= [object.strftime(fmt),fmt],
            __kw__ = {})
            

    elif isinstance(object, Post):
        return dict(
            __class__ = "Post",
            __args__ = [],
            __kw__ = dict(
                date = object.date,
                title = object.title,
                rst_text = object.rst_text,
                tags = object.tags))

    elif isinstance(object, Blog):
        return dict(
            __class__ = "Blog",
            __args__ = [object.title, object.entries],
            __kw__ = {})

    else:
        return json.JSONEncoder.default(o)


def blog_encode2(object):
    if isinstance(object, datetime.datetime):
        fmt = "%Y-%m-%dT%H:%M:%S"
        return dict(
            __class__ = "datetime.datetime.strptime",
            __args__= [object.strftime(fmt),fmt],
            __kw__ = {})
            
    else:
        try:
            encoding = object._json()
        except AttributeError:
            encoding = json.JSONEncoder.default(o)
        return encoding
    

def blog_decode(some_dict):
    if set(some_dict.keys()) == {"__class__", "__args__", "__kw__"}:
        class_ = eval(some_dict["__class__"])
        return class_(*some_dict["__args__"], **some_dict["__kw__"])
    else:
        return some_dict
    


if __name__ == "__main__":
    travel = Blog("Travel")
    travel.title = "derdoo"
    travel.append( Post( date = datetime.datetime(2016,6, 14, 1, 31,24),
                            title = "Dlo Bagari",
                            rst_text = " some other text",
                            tags = ("#233AS", "#SDE45S")))
    travel.append( Post( date = datetime.datetime(2016,6, 14, 1, 31,24),
                            title = "Dlo Bagari2",
                            rst_text = " some other text2",
                            tags = ("#455AS6", "#66E4567")))

    #output show how object translated from python to json notation
    #indent is formationg option, is mean 4 space as in python
    encoder = json.dumps(travel, indent=4, default = blog_encode2)
    print(encoder)

    #write json to file
    with open("temp.json","w",encoding="UTF-8") as target:
        json.dump(travel, target, separators=(',', ':'), default=blog_encode2)

    #read json file
    with open("temp.json", "r", encoding="UTF-8") as source:
        objects = json.load(source, object_hook=blog_decode)

    print(objects.title)



    #decode the json object using our blog_decode function, return
    #proper blog and post object
    blog_data = json.loads(encoder, object_hook = blog_decode)
    print(blog_data.title)
    
    #encoding yaml
    text = yaml.dump(travel)
    print("\n\n******yaml*******")
    print(text)
    #decoding yaml notation
    copy = yaml.load(text)
    print(copy.title)
    

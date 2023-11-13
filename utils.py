import json

def save(contents, filename:str = "mypickle.pk")->None:
    with open(filename, 'w') as fn:
        json.dump(contents,fn)

def load(filename:str = "mypickle.pk"):
    with open(filename, 'r') as fn:
        return json.load(fn)

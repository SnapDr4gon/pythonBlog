from models.tag import Tag

def createTag(name, url):
    tag = Tag(name, url)
    tag_dict = tag.__dict__

    return tag_dict

def readTag():
    name = input("Ingrese el nombre del tag a buscar: ")

    return name

def updateTag():
    name = input("Ingrese el nuevo nombre del tag: ")

    data = {
        "name": name
    }

    return data

def deleteTag():
    name = input("Ingrese el nombre del tag: ")

    return name
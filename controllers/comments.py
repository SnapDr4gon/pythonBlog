from models.comment import Comment

def createComment(name, url):
    comment = Comment(name, url)
    comment_dict = comment.__dict__

    return comment_dict

def readComment():
    name: input("Ingrese el nombre del comentario: ")

    return name

def updateComment():
    name = input("Ingrese el nombre del comentario: ")

    data = {
        "name": name
    }

    return data

def deleteComment():
    name = input("Ingrese el nombre del comentario: ")

    return name
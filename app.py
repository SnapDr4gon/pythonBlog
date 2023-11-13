from pymongo.mongo_client import MongoClient
from controllers.users import *
from controllers.articles import *
from controllers.comments import *
from controllers.categories import *
from controllers.tags import *
from bson import ObjectId

url = "mongodb://localhost:27017"

client = MongoClient(url)

try:
    client.admin.command('ping')
    print("Connection OK")

except Exception as e:
    print(e)
    exit()

db = client.blog

users = db.users
articles = db.articles
categories = db.categories
comments = db.comments
tags = db.tags

print("PYTHON CRUD")
print("1.-Users")
print("2.-Articles")
print("3.-Comments")
print("4.-Categories")
print("5.-Tags")
collection = int(input("Ingrese el numero de la categoria que desea modificar o ver: "))

def usersCRUD():
    print("Users CRUD")
    print("1.- Creat un usuario: ")
    print("2.- Leer la informacion de un usuario")
    print("3.- Actualizar la informacion de un usuario")
    print("4.- Eliminar a un usuario")
    opcion = int(input("Ingrese el numero de opcion a realizar: "))

    if (opcion == 1):
        name = input("Ingrese el nombre del usuario: ")
        email = input("Ingrese el email: ")
        user = createUser(name, email)
        users.insert_one(user).inserted_id
    elif(opcion == 2):
        name = readUser()
        user = users.find_one({ "name" : name })
        print(f"Esta es la informacion del usuario: \n{user}")
    elif(opcion == 3):
        userId = ObjectId(input("Ingrese el id del usuario a actualizar: "))
        existingUser = users.find_one({ "_id" : userId })

        if existingUser:
            updateData = updateUser()
            users.update_one({ "_id" : userId }, { "$set" : updateData })
        else:
            print("No")
    elif(opcion == 4):
        userName = deleteUser()
        users.delete_one({ "name" : userName })

def articlesCRUD():
    print("Articles CRUD")
    print("1.- Crear un articulo")
    print("2.- Leer un articulo")
    print("3.- Actualizar la informacion de un articulo")
    print("4.- Eliminar a un articulo")
    opcion = int(input("Ingrese el numero de opcion a realizar: "))

    if (opcion == 1):
        title = input("Ingrese el titulo del articulo: ")
        date = input("Ingrese la fecha de hoy: ")
        text = input("Ingrese el contenido del archivo: ")
        article = createArticle(title, date, text)
        articles.insert_one(article).inserted_id
    elif(opcion == 2):
        title = readArticle()
        article = articles.find_one({ "title" : title })
        print(f"Este es el articulo: \n{article}")
    elif(opcion == 3):
        articleId = ObjectId(input("Ingrese el id del articulo a actualizar: "))
        existingArticle = articles.find_one({ "_id" : articleId })

        if existingArticle:
            updateData = updateArticle()
            articles.update_one({ "_id" : articleId }, { "$set" : updateData })
        else:
            print("No")
    elif(opcion == 4):
        title = deleteArticle()
        articles.delete_one({ "title" : title })

def commentsCRUD():
    print("comments CRUD")
    print("1.- Crear un comentario")
    print("2.- Leer un comentario")
    print("3.- Actualizar un comentario")
    print("4.- Eliminar a un comentario")
    opcion = int(input("Ingrese el numero de opcion a realizar: "))

    if (opcion == 1):
        name = input("Ingrese el nombre del comentario: ")
        url = input("Ingrese el nombre del articulo del comentario: ")

        comment = createComment(name, url)
        comments.insert_one(comment).inserted_id
    elif(opcion == 2):
        name = readComment()
        comment = comments.find_one({ "name" : name })
        print(f"Este es el comentario: \n{comment}")
    elif(opcion == 3):
        commentId = ObjectId(input("Ingrese el id del comentario a actualizar: "))
        existingComment = comments.find_one({ "_id" : commentId })

        if existingComment:
            updateData = updateComment()
            comments.update_one({ "_id" : commentId }, { "$set" : updateData })
        else:
            print("No")
    elif(opcion == 4):
        name = deleteComment()
        comments.delete_one({ "name" : name })

def categoriesCRUD():
    print("categories CRUD")
    print("1.- Crear una categoria")
    print("2.- Ver una categoria")
    print("3.- Actualizar una categoria")
    print("4.- Eliminar una categoria")
    opcion = int(input("Ingrese el numero de opcion a realizar: "))

    if (opcion == 1):
        name = input("Ingrese el nombre de la categoria: ")
        url = input("Ingrese el nombre del articulo de la categoria: ")

        categorie = createCategorie(name, url)
        categories.insert_one(categorie).inserted_id
    elif(opcion == 2):
        name = readCategorie()
        categorie = categories.find_one({ "name" : name })
        print(f"Esta es la categoria: \n{categorie}")
    elif(opcion == 3):
        categorieId = ObjectId(input("Ingrese el id de la categoria a actualizar: "))
        existingCategorie = comments.find_one({ "_id" : categorieId })

        if existingCategorie:
            updateData = updateCategorie()
            categories.update_one({ "_id" : categorieId }, { "$set" : updateData })
        else:
            print("No")
    elif(opcion == 4):
        name = deleteCategorie()
        categories.delete_one({ "name" : name })

def tagsCRUD():
    print("tags CRUD")
    print("1.- Crear un tag")
    print("2.- Ver un tag")
    print("3.- Actualizar un tag")
    print("4.- Eliminar un tag")
    opcion = int(input("Ingrese el numero de opcion a realizar: "))

    if (opcion == 1):
        name = input("Ingrese el nombre del tag: ")
        url = input("Ingrese el nombre del articulo del tag: ")

        tag = createTag(name, url)
        tags.insert_one(tag).inserted_id
    elif(opcion == 2):
        name = readTag()
        tag = tags.find_one({ "name" : name })
        print(f"Esta es la categoria: \n{tag}")
    elif(opcion == 3):
        tagId = ObjectId(input("Ingrese el id del tag a actualizar: "))
        existingTag = tags.find_one({ "_id" : tagId })

        if existingTag:
            updateData = updateTag()
            tags.update_one({ "_id" : tagId }, { "$set" : updateData })
        else:
            print("No")
    elif(opcion == 4):
        name = deleteTag()
        tags.delete_one({ "name" : name })
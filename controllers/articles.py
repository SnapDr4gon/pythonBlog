from models.article import Article
import pymongo

def createArticle(title, date, text):
    article = Article(title, date, text, [], [])
    article_dict = article.__dict__

    return article_dict

def readArticle():
    name = input("Ingrese el nombre del articulo: ")

    return name

def updateArticle():
    title = input("Ingrese el nuevo titulo: ")
    date = input("Ingrese la fecha actual: ")
    text = input("Ingrese el nuevo contenido del articulo: ")

    data = {
        "title": title,
        "date": date,
        "text": text
    }

    return data

def deleteArticle():
    name = "Ingrese el nombre del articulo: "

    return name
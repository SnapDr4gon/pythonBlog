from models.categorie import Categorie

def createCategorie(name, url):
    categorie = Categorie(name, url)
    categorie_dict = categorie.__dict__

    return categorie_dict

def readCategorie():
    name = input("Ingrese el nombre de la categoria: ")

    return name

def updateCategorie():
    name = input("Ingrese el nuevo nombre de la categoria: ")
    url = input("Ingrese el nuevo url: ")

    data = {
        "name": name,
        "url": url
    }

    return data

def deleteCategorie():
    name = input("Ingrese el nombre de la categoria a eliminar: ")

    return name
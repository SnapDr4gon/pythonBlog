from models.user import User
import pymongo

def createUser(name, email):
    user = User(name, email, [], [])
    user_dict = user.__dict__

    return user_dict

def readUser():
    name = input("Ingrese el nombre del usuario: ")
    
    return name

def updateUser():
    name = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese el email del usuario: ")

    data = {
        "name": name,
        "email": email
    }

    return data

def deleteUser():
    name = input("Ingrese el nombre del usuario a eliminar: ")

    return name
from pymongo.mongo_client import MongoClient
from controllers.users import *
from controllers.articles import *
from controllers.comments import *
from controllers.categories import *
from controllers.tags import *
from bson import ObjectId
import tkinter as tk
from tkinter import messagebox

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

def show_menu():
    def handle_category(category):
        if category == 'Users':
            usersCRUD()
        elif category == 'Articles':
            articlesCRUD()
        elif category == 'Comments':
            commentsCRUD()
        elif category == 'Categories':
            categoriesCRUD()
        elif category == 'Tags':
            tagsCRUD()

    categories = ["Users", "Articles", "Comments", "Categories", "Tags"]

    menu_window = tk.Tk()
    menu_window.title("Python CRUD")

    label = tk.Label(menu_window, text="Seleccione una de las siguientes opciones a trabajar:")
    label.pack(pady=10)  

    frame = tk.Frame(menu_window)
    frame.pack()

    for category in categories:
        category_button = tk.Button(frame, text=category, command=lambda c=category: handle_category(c))
        category_button.pack(side=tk.LEFT, padx=5)

    menu_window.mainloop()

def usersCRUD():
    def create_user():
        name = name_entry.get()
        email = email_entry.get()
        user = createUser(name, email)
        users.insert_one(user).inserted_id
        messagebox.showinfo("Éxito", "Usuario creado exitosamente")

    def read_user():
        user_info_label.config(text=f"Lista de usuarios:\n{users.find()}")

    def update_user():
        user_id = ObjectId(id_entry.get())
        existing_user = users.find_one({"_id": user_id})

        if existing_user:
            update_data = updateUser()
            users.update_one({"_id": user_id}, {"$set": update_data})
            messagebox.showinfo("Éxito", "Información de usuario actualizada")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def delete_user():
        user_name = name_entry.get()
        result = users.delete_one({"name": user_name})
        if result.deleted_count > 0:
            messagebox.showinfo("Éxito", "Usuario eliminado exitosamente")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    user_window = tk.Toplevel()
    user_window.title("Users CRUD")

    name_label = tk.Label(user_window, text="Nombre del usuario:")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_entry = tk.Entry(user_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    email_label = tk.Label(user_window, text="Email del usuario:")
    email_label.grid(row=1, column=0, padx=5, pady=5)

    email_entry = tk.Entry(user_window)
    email_entry.grid(row=1, column=1, padx=5, pady=5)

    id_label = tk.Label(user_window, text="ID del usuario (para actualizar):")
    id_label.grid(row=2, column=0, padx=5, pady=5)

    id_entry = tk.Entry(user_window)
    id_entry.grid(row=2, column=1, padx=5, pady=5)

    create_button = tk.Button(user_window, text="Crear Usuario", command=create_user)
    create_button.grid(row=3, column=0, columnspan=2, pady=10)

    read_button = tk.Button(user_window, text="Leer Usuario", command=read_user)
    read_button.grid(row=4, column=0, columnspan=2, pady=10)

    update_button = tk.Button(user_window, text="Actualizar Usuario", command=update_user)
    update_button.grid(row=5, column=0, columnspan=2, pady=10)

    delete_button = tk.Button(user_window, text="Eliminar Usuario", command=delete_user)
    delete_button.grid(row=6, column=0, columnspan=2, pady=10)

    user_info_label = tk.Label(user_window, text="")
    user_info_label.grid(row=7, column=0, columnspan=2, pady=10)

def articlesCRUD():
    def create_article():
        title = title_entry.get()
        date = date_entry.get()
        text = text_entry.get("1.0", tk.END)  # Obtiene el contenido del Entry de texto

        article = createArticle(title, date, text)
        articles.insert_one(article).inserted_id
        messagebox.showinfo("Éxito", "Artículo creado exitosamente")

    def read_article():
        article_info_label.config(text=f"Información del artículo:\n{articles.find()}")

    def update_article():
        article_id = ObjectId(id_entry.get())
        existing_article = articles.find_one({"_id": article_id})

        if existing_article:
            update_data = updateArticle()
            articles.update_one({"_id": article_id}, {"$set": update_data})
            messagebox.showinfo("Éxito", "Información de artículo actualizada")
        else:
            messagebox.showerror("Error", "Artículo no encontrado")

    def delete_article():
        article_title = title_entry.get()
        result = articles.delete_one({"title": article_title})
        if result.deleted_count > 0:
            messagebox.showinfo("Éxito", "Artículo eliminado exitosamente")
        else:
            messagebox.showerror("Error", "Artículo no encontrado")

    article_window = tk.Toplevel()
    article_window.title("Articles CRUD")

    title_label = tk.Label(article_window, text="Título del artículo:")
    title_label.grid(row=0, column=0, padx=5, pady=5)

    title_entry = tk.Entry(article_window)
    title_entry.grid(row=0, column=1, padx=5, pady=5)

    date_label = tk.Label(article_window, text="Fecha del artículo:")
    date_label.grid(row=1, column=0, padx=5, pady=5)

    date_entry = tk.Entry(article_window)
    date_entry.grid(row=1, column=1, padx=5, pady=5)

    text_label = tk.Label(article_window, text="Contenido del artículo:")
    text_label.grid(row=2, column=0, padx=5, pady=5)

    text_entry = tk.Text(article_window, height=5, width=30)
    text_entry.grid(row=2, column=1, padx=5, pady=5)

    id_label = tk.Label(article_window, text="ID del artículo (para actualizar):")
    id_label.grid(row=3, column=0, padx=5, pady=5)

    id_entry = tk.Entry(article_window)
    id_entry.grid(row=3, column=1, padx=5, pady=5)

    create_button = tk.Button(article_window, text="Crear Artículo", command=create_article)
    create_button.grid(row=4, column=0, columnspan=2, pady=10)

    read_button = tk.Button(article_window, text="Leer Artículo", command=read_article)
    read_button.grid(row=5, column=0, columnspan=2, pady=10)

    update_button = tk.Button(article_window, text="Actualizar Artículo", command=update_article)
    update_button.grid(row=6, column=0, columnspan=2, pady=10)

    delete_button = tk.Button(article_window, text="Eliminar Artículo", command=delete_article)
    delete_button.grid(row=7, column=0, columnspan=2, pady=10)

    article_info_label = tk.Label(article_window, text="")
    article_info_label.grid(row=8, column=0, columnspan=2, pady=10)

def commentsCRUD():
    def create_comment():
        name = name_entry.get()
        url = url_entry.get()
        comment = createComment(name, url)
        comments.insert_one(comment).inserted_id
        messagebox.showinfo("Éxito", "Comentario creado exitosamente")

    def read_comment():
        comment_info_label.config(text=f"Lista de comentarios:\n{comments.find()}")

    def update_comment():
        comment_id = ObjectId(id_entry.get())
        existing_comment = comments.find_one({"_id": comment_id})

        if existing_comment:
            update_data = updateComment()
            comments.update_one({"_id": comment_id}, {"$set": update_data})
            messagebox.showinfo("Éxito", "Información de comentario actualizada")
        else:
            messagebox.showerror("Error", "Comentario no encontrado")

    def delete_comment():
        comment_name = name_entry.get()
        result = comments.delete_one({"name": comment_name})
        if result.deleted_count > 0:
            messagebox.showinfo("Éxito", "Comentario eliminado exitosamente")
        else:
            messagebox.showerror("Error", "Comentario no encontrado")

    comment_window = tk.Toplevel()
    comment_window.title("Comments CRUD")

    name_label = tk.Label(comment_window, text="Nombre del comentario:")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_entry = tk.Entry(comment_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    url_label = tk.Label(comment_window, text="URL del artículo del comentario:")
    url_label.grid(row=1, column=0, padx=5, pady=5)

    url_entry = tk.Entry(comment_window)
    url_entry.grid(row=1, column=1, padx=5, pady=5)

    id_label = tk.Label(comment_window, text="ID del comentario (para actualizar):")
    id_label.grid(row=2, column=0, padx=5, pady=5)

    id_entry = tk.Entry(comment_window)
    id_entry.grid(row=2, column=1, padx=5, pady=5)

    create_button = tk.Button(comment_window, text="Crear Comentario", command=create_comment)
    create_button.grid(row=3, column=0, columnspan=2, pady=10)

    read_button = tk.Button(comment_window, text="Leer Comentario", command=read_comment)
    read_button.grid(row=4, column=0, columnspan=2, pady=10)

    update_button = tk.Button(comment_window, text="Actualizar Comentario", command=update_comment)
    update_button.grid(row=5, column=0, columnspan=2, pady=10)

    delete_button = tk.Button(comment_window, text="Eliminar Comentario", command=delete_comment)
    delete_button.grid(row=6, column=0, columnspan=2, pady=10)

    comment_info_label = tk.Label(comment_window, text="")
    comment_info_label.grid(row=7, column=0, columnspan=2, pady=10)

def categoriesCRUD():
    def create_categorie():
        name = name_entry.get()
        article_name = article_name_entry.get()
        category = createCategorie(name, article_name)
        categories.insert_one(category).inserted_id
        messagebox.showinfo("Éxito", "Categoría creada exitosamente")

    def read_categorie():
        category_info_label.config(text=f"Lista de categorias:\n{categories.find()}")

    def update_categorie():
        category_id = ObjectId(id_entry.get())
        existing_category = categories.find_one({"_id": category_id})

        if existing_category:
            update_data = updateCategorie()
            categories.update_one({"_id": category_id}, {"$set": update_data})
            messagebox.showinfo("Éxito", "Información de categoría actualizada")
        else:
            messagebox.showerror("Error", "Categoría no encontrada")

    def delete_categorie():
        category_name = name_entry.get()
        result = categories.delete_one({"name": category_name})
        if result.deleted_count > 0:
            messagebox.showinfo("Éxito", "Categoría eliminada exitosamente")
        else:
            messagebox.showerror("Error", "Categoría no encontrada")

    categorie_window = tk.Toplevel()
    categorie_window.title("Categories CRUD")

    name_label = tk.Label(categorie_window, text="Nombre de la categoría:")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_entry = tk.Entry(categorie_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    article_name_label = tk.Label(categorie_window, text="Nombre del artículo de la categoría:")
    article_name_label.grid(row=1, column=0, padx=5, pady=5)

    article_name_entry = tk.Entry(categorie_window)
    article_name_entry.grid(row=1, column=1, padx=5, pady=5)

    id_label = tk.Label(categorie_window, text="ID de la categoría (para actualizar):")
    id_label.grid(row=2, column=0, padx=5, pady=5)

    id_entry = tk.Entry(categorie_window)
    id_entry.grid(row=2, column=1, padx=5, pady=5)

    create_button = tk.Button(categorie_window, text="Crear Categoría", command=create_categorie)
    create_button.grid(row=3, column=0, columnspan=2, pady=10)

    read_button = tk.Button(categorie_window, text="Ver Categoría", command=read_categorie)
    read_button.grid(row=4, column=0, columnspan=2, pady=10)

    update_button = tk.Button(categorie_window, text="Actualizar Categoría", command=update_categorie)
    update_button.grid(row=5, column=0, columnspan=2, pady=10)

    delete_button = tk.Button(categorie_window, text="Eliminar Categoría", command=delete_categorie)
    delete_button.grid(row=6, column=0, columnspan=2, pady=10)

    category_info_label = tk.Label(categorie_window, text="")
    category_info_label.grid(row=7, column=0, columnspan=2, pady=10)

def tagsCRUD():
    def create_tag():
        name = name_entry.get()
        article_name = article_name_entry.get()
        tag = createTag(name, article_name)
        tags.insert_one(tag).inserted_id
        messagebox.showinfo("Éxito", "Tag creado exitosamente")

    def read_tag():
        tag_info_label.config(text=f"Información del tag:\n{tags.find()}")

    def update_tag():
        tag_id = ObjectId(id_entry.get())
        existing_tag = tags.find_one({"_id": tag_id})

        if existing_tag:
            update_data = updateTag()
            tags.update_one({"_id": tag_id}, {"$set": update_data})
            messagebox.showinfo("Éxito", "Información de tag actualizada")
        else:
            messagebox.showerror("Error", "Tag no encontrado")

    def delete_tag():
        tag_name = name_entry.get()
        result = tags.delete_one({"name": tag_name})
        if result.deleted_count > 0:
            messagebox.showinfo("Éxito", "Tag eliminado exitosamente")
        else:
            messagebox.showerror("Error", "Tag no encontrado")

    tag_window = tk.Toplevel()
    tag_window.title("Tags CRUD")

    name_label = tk.Label(tag_window, text="Nombre del tag:")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_entry = tk.Entry(tag_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    article_name_label = tk.Label(tag_window, text="Nombre del artículo del tag:")
    article_name_label.grid(row=1, column=0, padx=5, pady=5)

    article_name_entry = tk.Entry(tag_window)
    article_name_entry.grid(row=1, column=1, padx=5, pady=5)

    id_label = tk.Label(tag_window, text="ID del tag (para actualizar):")
    id_label.grid(row=2, column=0, padx=5, pady=5)

    id_entry = tk.Entry(tag_window)
    id_entry.grid(row=2, column=1, padx=5, pady=5)

    create_button = tk.Button(tag_window, text="Crear Tag", command=create_tag)
    create_button.grid(row=3, column=0, columnspan=2, pady=10)

    read_button = tk.Button(tag_window, text="Ver Tag", command=read_tag)
    read_button.grid(row=4, column=0, columnspan=2, pady=10)

    update_button = tk.Button(tag_window, text="Actualizar Tag", command=update_tag)
    update_button.grid(row=5, column=0, columnspan=2, pady=10)

    delete_button = tk.Button(tag_window, text="Eliminar Tag", command=delete_tag)
    delete_button.grid(row=6, column=0, columnspan=2, pady=10)

    tag_info_label = tk.Label(tag_window, text="")
    tag_info_label.grid(row=7, column=0, columnspan=2, pady=10)
        
show_menu()

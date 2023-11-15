import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

# Conectarse a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mi_base_de_datos']

# Definir las colecciones
users_collection = db['users']
articles_collection = db['articles']
comments_collection = db['comments']
tags_collection = db['tags']
categories_collection = db['categories']

# Funciones CRUD
def create_document(collection, data):
    return collection.insert_one(data).inserted_id

def read_documents(collection):
    return list(collection.find())

def update_document(collection, filter_data, update_data):
    collection.update_one(filter_data, {'$set': update_data})

def delete_document(collection, filter_data):
    collection.delete_one(filter_data)

# Interfaz gráfica con Tkinter
class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD App")

        self.tab_control = ttk.Notebook(root)

        # Tabla de usuarios
        self.users_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.users_tab, text='Users')
        self.create_user_interface()

        # Add tabs for other interfaces
        self.articles_tab = ttk.Frame(self.tab_control)
        self.create_articles_interface()  # Call the method before adding the tab
        self.tab_control.add(self.articles_tab, text='Articles')

        self.comments_tab = ttk.Frame(self.tab_control)
        self.create_comments_interface()  # Call the method before adding the tab
        self.tab_control.add(self.comments_tab, text='Comments')

        self.tags_tab = ttk.Frame(self.tab_control)
        self.create_tags_interface()  # Call the method before adding the tab
        self.tab_control.add(self.tags_tab, text='Tags')

        self.categories_tab = ttk.Frame(self.tab_control)
        self.create_categories_interface()  # Call the method before adding the tab
        self.tab_control.add(self.categories_tab, text='Categories')

        self.tab_control.pack(expand=1, fill='both')

    def create_user_interface(self):
        # Etiquetas y campos de entrada para Users
        tk.Label(self.users_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.users_tab, text="Email:").grid(row=1, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(self.users_tab)
        self.email_entry = tk.Entry(self.users_tab)

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botones CRUD para Users
        tk.Button(self.users_tab, text="Create User", command=self.create_user).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.users_tab, text="Read Users", command=self.read_users).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.users_tab, text="Update User", command=self.update_user).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.users_tab, text="Delete User", command=self.delete_user).grid(row=5, column=0, columnspan=2, pady=10)

    def create_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()

        if name and email:
            user_data = {'name': name, 'email': email}
            create_document(users_collection, user_data)
            print("User created successfully!")
        else:
            print("Name and email are required.")

    def read_users(self):
        users = read_documents(users_collection)
        for user in users:
            print(user)

    def update_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()

        if name and email:
            filter_data = {'name': name}
            update_data = {'email': email}
            update_document(users_collection, filter_data, update_data)
            print("User updated successfully!")
        else:
            print("Name and email are required.")

    def delete_user(self):
        name = self.name_entry.get()

        if name:
            filter_data = {'name': name}
            delete_document(users_collection, filter_data)
            print("User deleted successfully!")
        else:
            print("Name is required.")
    
    def create_articles_interface(self):
        # Etiquetas y campos de entrada para Articles
        tk.Label(self.articles_tab, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.articles_tab, text="Date:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.articles_tab, text="Text:").grid(row=2, column=0, padx=5, pady=5)

        self.title_entry = tk.Entry(self.articles_tab)
        self.date_entry = tk.Entry(self.articles_tab)
        self.text_entry = tk.Entry(self.articles_tab)

        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)
        self.text_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones CRUD para Articles
        tk.Button(self.articles_tab, text="Create Article", command=self.create_article).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.articles_tab, text="Read Articles", command=self.read_articles).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.articles_tab, text="Update Article", command=self.update_article).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.articles_tab, text="Delete Article", command=self.delete_article).grid(row=6, column=0, columnspan=2, pady=10)

    def create_article(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        text = self.text_entry.get()

        if title and date and text:
            article_data = {'title': title, 'date': date, 'text': text}
            create_document(articles_collection, article_data)
            print("Article created successfully!")
        else:
            print("Title, date, and text are required.")

    def read_articles(self):
        articles = read_documents(articles_collection)
        for article in articles:
            print(article)

    def update_article(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        text = self.text_entry.get()

        if title and date and text:
            filter_data = {'title': title}
            update_data = {'date': date, 'text': text}
            update_document(articles_collection, filter_data, update_data)
            print("Article updated successfully!")
        else:
            print("Title, date, and text are required.")

    def delete_article(self):
        title = self.title_entry.get()

        if title:
            filter_data = {'title': title}
            delete_document(articles_collection, filter_data)
            print("Article deleted successfully!")
        else:
            print("Title is required.")
    
    def create_comments_interface(self):
        # Etiquetas y campos de entrada para Comments
        tk.Label(self.comments_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.comments_tab, text="URL:").grid(row=1, column=0, padx=5, pady=5)

        self.comment_name_entry = tk.Entry(self.comments_tab)
        self.comment_url_entry = tk.Entry(self.comments_tab)

        self.comment_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.comment_url_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botones CRUD para Comments
        tk.Button(self.comments_tab, text="Create Comment", command=self.create_comment).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.comments_tab, text="Read Comments", command=self.read_comments).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.comments_tab, text="Update Comment", command=self.update_comment).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.comments_tab, text="Delete Comment", command=self.delete_comment).grid(row=5, column=0, columnspan=2, pady=10)

    def create_comment(self):
        name = self.comment_name_entry.get()
        url = self.comment_url_entry.get()

        if name and url:
            comment_data = {'name': name, 'url': url}
            create_document(comments_collection, comment_data)
            print("Comment created successfully!")
        else:
            print("Name and URL are required.")

    def read_comments(self):
        comments = read_documents(comments_collection)
        for comment in comments:
            print(comment)

    def update_comment(self):
        name = self.comment_name_entry.get()
        url = self.comment_url_entry.get()

        if name and url:
            filter_data = {'name': name}
            update_data = {'url': url}
            update_document(comments_collection, filter_data, update_data)
            print("Comment updated successfully!")
        else:
            print("Name and URL are required.")

    def delete_comment(self):
        name = self.comment_name_entry.get()

        if name:
            filter_data = {'name': name}
            delete_document(comments_collection, filter_data)
            print("Comment deleted successfully!")
        else:
            print("Name is required.")

    def create_tags_interface(self):
        # Etiquetas y campos de entrada para Tags
        tk.Label(self.tags_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.tags_tab, text="URL:").grid(row=1, column=0, padx=5, pady=5)

        self.tag_name_entry = tk.Entry(self.tags_tab)
        self.tag_url_entry = tk.Entry(self.tags_tab)

        self.tag_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.tag_url_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botones CRUD para Tags
        tk.Button(self.tags_tab, text="Create Tag", command=self.create_tag).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.tags_tab, text="Read Tags", command=self.read_tags).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.tags_tab, text="Update Tag", command=self.update_tag).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.tags_tab, text="Delete Tag", command=self.delete_tag).grid(row=5, column=0, columnspan=2, pady=10)

    def create_tag(self):
        name = self.tag_name_entry.get()
        url = self.tag_url_entry.get()

        if name and url:
            tag_data = {'name': name, 'url': url}
            create_document(tags_collection, tag_data)
            print("Tag created successfully!")
        else:
            print("Name and URL are required.")

    def read_tags(self):
        tags = read_documents(tags_collection)
        for tag in tags:
            print(tag)

    def update_tag(self):
        name = self.tag_name_entry.get()
        url = self.tag_url_entry.get()

        if name and url:
            filter_data = {'name': name}
            update_data = {'url': url}
            update_document(tags_collection, filter_data, update_data)
            print("Tag updated successfully!")
        else:
            print("Name and URL are required.")

    def delete_tag(self):
        name = self.tag_name_entry.get()

        if name:
            filter_data = {'name': name}
            delete_document(tags_collection, filter_data)
            print("Tag deleted successfully!")
        else:
            print("Name is required.")

    def create_categories_interface(self):
        # Etiquetas y campos de entrada para Categories
        tk.Label(self.categories_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.categories_tab, text="URL:").grid(row=1, column=0, padx=5, pady=5)

        self.category_name_entry = tk.Entry(self.categories_tab)
        self.category_url_entry = tk.Entry(self.categories_tab)

        self.category_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.category_url_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botones CRUD para Categories
        tk.Button(self.categories_tab, text="Create Category", command=self.create_category).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.categories_tab, text="Read Categories", command=self.read_categories).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.categories_tab, text="Update Category", command=self.update_category).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.categories_tab, text="Delete Category", command=self.delete_category).grid(row=5, column=0, columnspan=2, pady=10)

    def create_category(self):
        name = self.category_name_entry.get()
        url = self.category_url_entry.get()

        if name and url:
            category_data = {'name': name, 'url': url}
            create_document(categories_collection, category_data)
            print("Category created successfully!")
        else:
            print("Name and URL are required.")

    def read_categories(self):
        categories = read_documents(categories_collection)
        for category in categories:
            print(category)

    def update_category(self):
        name = self.category_name_entry.get()
        url = self.category_url_entry.get()

        if name and url:
            filter_data = {'name': name}
            update_data = {'url': url}
            update_document(categories_collection, filter_data, update_data)
            print("Category updated successfully!")
        else:
            print("Name and URL are required.")

    def delete_category(self):
        name = self.category_name_entry.get()

        if name:
            filter_data = {'name': name}
            delete_document(categories_collection, filter_data)
            print("Category deleted successfully!")
        else:
            print("Name is required.")

# Inicializar la aplicación Tkinter
root = tk.Tk()
app = CRUDApp(root)
root.mainloop()

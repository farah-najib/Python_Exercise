from pymongo import MongoClient
from pymongo.server_api import ServerApi

import certifi
ca = certifi.where()

def get_database():
  CONNECTION_STRING = "mongodb+srv://farahengnajib:E1bHFKVDHqW4T95e@cluster0.cmmqk0x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
  client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'), tlsCAFile=ca)
  return client['book_store']

dbname = get_database()
collection_name = dbname["books"]

def add_book():
  item = {
    "title": "The Definitive Guide to MongoDB",
    "price": 710.52,
    "curreny": "SEK",
    "author": "Peter Membrey",
    "stock": 20
  }
  collection_name.insert_many([item])

def view_all_books():
  item_details = collection_name.find()
  for item in item_details:
    print(item)

def search_by_title(title):
  item_details = collection_name.find({"title": title})
  for item in item_details:
    print(item)

def search_by_auther(author):
  item_details = collection_name.find({"author": author})
  for item in item_details:
    print(item)

def deleted_book_by_title(title):
  collection_name.delete_one({"title": title})

def update_book_price_by_title(title, price):
  collection_name.update_one({"title": title}, { "$set": { "price": price } })

def search_books_in_stock():
  item_details = collection_name.find({"stock": {"$gt": 0}})
  for item in item_details:
    print(item)

print("Add a book")
add_book()

print("View all books")
view_all_books()
print("$$$$$")

print("Search a book by title")
search_by_title("The Definitive Guide to MongoDB")
print("$$$$$")

print("Update a book price")
update_book_price_by_title("The Definitive Guide to MongoDB", 10)
print("$$$$$")

print("Delete a book")
deleted_book_by_title("The Definitive Guide to MongoDB")
print("$$$$$")

print("View books by author")
search_by_auther("Peter Membrey")
print("$$$$$")

print("View books in Stock")
search_books_in_stock()
print("$$$$$")

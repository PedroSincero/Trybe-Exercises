# ❗ Importe o arquivo books.json no MongoDB antes de responder as próximas questões.
# https://s3.us-east-2.amazonaws.com/assets.app.betrybe.com/computer-science/python/entrada-saida/books-346aab4788ea58d4c3aa988632da100b.json
# 🦜 mongoimport --db library books.json
# Exercício 6 Escreva um programa que se conecte ao banco de dados library e liste os livros da coleção books para uma determinada categoria recebida por uma pessoa usuária. Somente o título dos livros deve ser exibido.

from pymongo import MongoClient


category = input("Escolha uma categoria: ")
with MongoClient() as client:
    db = client.library
    for book in db.books.find({"categories": category}, projection=["title"]):
        print(book["title"])
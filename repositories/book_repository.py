from cProfile import run
from unittest import result
from db.run_sql import run_sql
from models.book import Book
import repositories.author_repository as author_repository

def save(book):
    sql = """INSERT INTO books (title, genre, author_id) VALUES (%s, %s, %s) RETURNING *"""
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row["author_id"])
        book = Book(row["title"], row["genre"], author, row["id"])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        author = author_repository.select(result["author_id"])
        book = Book(result["title"], result["genre"], author, row["id"])
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)
from flask import Flask, redirect, render_template, Blueprint
from models.book import Book
import repositories.book_repository as book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("/books/index.html", books = books)

@books_blueprint.route("/books/<id>/delete", methods = ["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

@books_blueprint.route("/books/<id>", methods=["GET"])
def show_book(id):
    found_book = book_repository.select(id)
    return render_template("books/show.html", book = found_book)


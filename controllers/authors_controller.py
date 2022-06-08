from flask import Flask, render_template, Blueprint
from models.author import Author
import repositories.author_repository as author_repository

authors_blueprint = Blueprint("authors", __name__)

@authors_blueprint.route("/authors")
def books():
    authors = author_repository.select_all()
    return render_template("/authors/index.html")
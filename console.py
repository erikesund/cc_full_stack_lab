import pdb
from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("J. R. R. Tolkein")
author_2 = Author("F. Scott Fitzgerald")
author_3 = Author("Erik Sund")
author_4 = Author("Moath Alzoubi")

book_1 = Book("The Lord of the Rings", "fantasy", author_1)
book_2 = Book("The Great Gatsby", "fiction", author_2)
book_3 = Book("The Power of Hats", "fashion", author_3)
book_4 = Book("The Hobbit Guide", "non-fiction", author_4)
book_5 = Book("The Hobbit", "fantasy", author_1)

author_repository.save(author_1)
author_repository.save(author_2)
author_repository.save(author_3)
author_repository.save(author_4)

book_repository.save(book_1)
book_repository.save(book_2)
book_repository.save(book_3)
book_repository.save(book_4)
book_repository.save(book_5)

pdb.set_trace()
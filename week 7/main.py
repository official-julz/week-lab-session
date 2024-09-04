# main.py
from book import Book
from library import Library

# create some book objects
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Science Essentials", "Alice Johnson")
book3 = Book("Wed Development Basics", "Bob Wilson")

# create a library
library = Library()

# Add book to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# borrow and return books
print(library.borrow_book("Python Programming"))  #Borrow book1
print(library.borrow_book("Python Programming"))  #Already borrowed
print(library.return_book("Python Programming"))  # Return book1
print(library.return_book("Python Programming"))  #Not currently borrowed

# coubt how many books are currently borrowed
print(f"Number of borrowed books: {library.borrowed_count}")
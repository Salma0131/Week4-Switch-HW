# Option B: Library Management System with a List of Book Objects

class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []  # List of Book objects

    def add_book(self, title, author, genre, year):
        book = Book(title, author, genre, year)
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return "Book not found."

    def find_by_author(self, author):
        result = [book for book in self.books if book.author == author]
        return result if result else "No books found for this author."


# Example Usage
library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925)
library.add_book("1984", "George Orwell", "Dystopian", 1949)

print(library.find_by_title("1984"))
print(library.find_by_author("F. Scott Fitzgerald"))

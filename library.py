# Define the Book class 
class Book:
    def __init__(self, title, call_number, author, num_copies):
        self.title = title
        self.call_number = call_number
        self.author = author
        self.num_copies = num_copies

    def check_availability(self):
        return self.num_copies > 0

    def check_out(self):
        if self.check_availability():
            self.num_copies -= 1

    def return_book(self):
        self.num_copies += 1

# Define the BackEndLibrary class 
class BackEndLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, title, call_number, author, num_copies):
        book = Book(title, call_number, author, num_copies)
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def checkout(self, title):
        book = self.find_book(title)
        if book and book.check_availability():
            book.check_out()
            return True
        return False

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
            return True
        return False

    def display_available_books(self):
        available_books = [book for book in self.books if book.check_availability()]
        return available_books

# Define the FrontEndLibrary class 
class FrontEndLibrary:
    def __init__(self, back_end_library):
        self.back_end_library = back_end_library

    def find_book(self, title):
        return self.back_end_library.find_book(title)

    def checkout(self, title):
        return self.back_end_library.checkout(title)

    def return_book(self, title):
        return self.back_end_library.return_book(title)

    def display_available_books(self):
        return self.back_end_library.display_available_books()

# Create a BackEndLibrary instance
library_backend = BackEndLibrary()

# Add books to the library
library_backend.add_book("Book 1", "001", "Author A", 5)
library_backend.add_book("Book 2", "002", "Author B", 3)
library_backend.add_book("Book 3", "003", "Author C", 2)

# Create a FrontEndLibrary instance using the BackEndLibrary
library_frontend = FrontEndLibrary(library_backend)

# Example usage:
print("Available Books:")
available_books = library_frontend.display_available_books()
for book in available_books:
    print(f"{book.title} by {book.author} (Call Number: {book.call_number})")

print("\nChecking out 'Book 1'...")
if library_frontend.checkout("Book 1"):
    print("Checked out successfully.")
else:
    print("Book not available for checkout.")

print("\nReturning 'Book 1'...")
if library_frontend.return_book("Book 1"):
    print("Returned successfully.")
else:
    print("Book return failed.")

# Display available books again after checking out and returning
print("\nAvailable Books:")
available_books = library_frontend.display_available_books()
for book in available_books:
    print(f"{book.title} by {book.author} (Call Number: {book.call_number})")

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def matches(self, keyword):
        return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))
        print("Book added successfully.\n")

    def list_books(self):
        if not self.books:
            print("No books in the library.\n")
            return
        print("Books in Library:")
        for book in self.books:
            print(book)
        print()

    def search_books(self, keyword):
        results = [book for book in self.books if book.matches(keyword)]
        if results:
            for book in results:
                print(book)
        else:
            print("No matching books found.")
        print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.borrow()
                print(f"You borrowed '{book.title}'.\n")
                return
        print("Book not available.\n")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.return_book()
                print(f"You returned '{book.title}'.\n")
                return
        print("Book not found or already returned.\n")


def library_menu():
    library = Library()

    while True:
        print("Library Menu:")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            library.add_book(title, author, year)
        elif choice == "2":
            library.list_books()
        elif choice == "3":
            keyword = input("Enter title or author: ")
            library.search_books(keyword)
        elif choice == "4":
            title = input("Enter title to borrow: ")
            library.borrow_book(title)
        elif choice == "5":
            title = input("Enter title to return: ")
            library.return_book(title)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


library_menu()

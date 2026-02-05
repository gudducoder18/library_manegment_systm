class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                return f.read().splitlines()
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.filename, "w") as f:
            for book in self.books:
                f.write(book + "\n")

    def add_book(self, book_name):
        self.books.append(book_name)
        self.save_books()
        print("✅ Book added successfully")

    def show_books(self):
        if not self.books:
            print("❌ No books available")
        else:
            print("\n📚 Available Books:")
            for book in self.books:
                print("-", book)

    def issue_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.save_books()
            print("📕 Book issued successfully")
        else:
            print("❌ Book not available")

    def return_book(self, book_name):
        self.books.append(book_name)
        self.save_books()
        print("📗 Book returned successfully")


def menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")


library = Library()

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "5":
        print("👋 Thank you for using Library System")
        break

    else:
        print("❌ Invalid choice")

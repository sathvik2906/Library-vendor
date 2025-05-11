import json
import os

class LibraryVendingMachine:
    def __init__(self, data_file="library_data.json"):
        self.data_file = data_file
        self.books = {}
        self.borrowed_books = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.books = data.get("books", {})
                self.borrowed_books = data.get("borrowed_books", {})
        else:
            # Initialize with default data
            self.books = {
                "1984": 3,
                "To Kill a Mockingbird": 2,
                "The Great Gatsby": 4,
                "Pride and Prejudice": 1
            }
            self.borrowed_books = {}

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump({
                "books": self.books,
                "borrowed_books": self.borrowed_books
            }, f, indent=4)

    def display_books(self):
        print("\nAvailable Books:")
        for title, qty in self.books.items():
            print(f" - {title} ({qty} available)")

    def borrow_book(self, user, title):
        if title not in self.books:
            print(f"Book '{title}' is not in the catalog.")
            return
        if self.books[title] == 0:
            print(f"Book '{title}' is currently not available.")
            return
        self.books[title] -= 1
        self.borrowed_books.setdefault(user, []).append(title)
        self.save_data()
        print(f"{user} borrowed '{title}'.")

    def return_book(self, user, title):
        if title not in self.books or title not in self.borrowed_books.get(user, []):
            print(f"{user} has not borrowed '{title}'.")
            return
        self.books[title] += 1
        self.borrowed_books[user].remove(title)
        self.save_data()
        print(f"{user} returned '{title}'.")

    def user_books(self, user):
        books = self.borrowed_books.get(user, [])
        print(f"{user} has borrowed: {books if books else 'No books'}")


# Example usage
if __name__ == "__main__":
    library = LibraryVendingMachine()

    while True:
        print("\n--- Library Vending Machine ---")
        print("1. Show available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View my borrowed books")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            user = input("Enter your name: ")
            title = input("Enter the book title to borrow: ")
            library.borrow_book(user, title)
        elif choice == '3':
            user = input("Enter your name: ")
            title = input("Enter the book title to return: ")
            library.return_book(user, title)
        elif choice == '4':
            user = input("Enter your name: ")
            library.user_books(user)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")




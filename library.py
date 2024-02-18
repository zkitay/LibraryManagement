class Library:
    def __init__(self):
        # Open the books.txt file in append and read mode
        self.file = open("books.txt", "a+")

    def __del__(self):
        # Close the books.txt file when the instance is destroyed
        self.file.close()

    def list_books(self):
        # Read and print all books
        self.file.seek(0)  # Go to the beginning of the file
        for book in self.file:
            print(book.strip())

    def add_book(self, title, author, release_year, pages):
        # Add a new book
        self.file.write(f"{title}, {author}, {release_year}, {pages}\n")

    def remove_book(self, title):
        # Remove a book by title
        self.file.seek(0)
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        for line in lines:
            if not line.startswith(title):
                self.file.write(line)


# Main program
lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        release_year = input("Enter the release year: ")
        pages = input("Enter the number of pages: ")
        lib.add_book(title, author, release_year, pages)
    elif choice == "3":
        title = input("Enter the title of the book to remove: ")
        lib.remove_book(title)
    elif choice == "4":
        break
    else:
        print("Invalid choice, please try again.")

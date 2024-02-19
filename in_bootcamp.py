class Library:
    def __init__(self):
        # Constructor method to open the books.txt file in append mode (a+)
        self.file = open("books.txt", "a+")

    def __del__(self):
        # Destructor method to close the file when the object is destroyed
        self.file.close()

    def list_books(self):
        # Method to list all books in the books.txt file
        # Seek to the beginning of the file
        self.file.seek(0)
        # Read all lines from the file
        books = self.file.readlines()
        if not books:
            # If no books are found, print a message
            print("No books found.")
        else:
            # If books are found, print their titles and authors
            print("List of Books:")
            for book in books:
                # Split each line into book information
                book_info = book.strip().split(",")
                # Print title and author of each book
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        # Method to add a new book to the books.txt file
        # Prompt user for book details
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")

        # Format book information as a string
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        # Write the book information to the file
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        # Method to remove a book from the books.txt file
        # Prompt user for the title of the book to be removed
        title = input("Enter the title of the book to remove: ")
        # Read all lines from the file
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []

        found = False
        # Iterate through each book in the file
        for book in books:
            # Split the book information into parts
            book_info = book.strip().split(",")
            if book_info[0] == title:
                # If the title matches, set found flag to True
                found = True
            else:
                # If the title doesn't match, add the book to updated_books list
                updated_books.append(book)

        if not found:
            # If book not found, print a message
            print("Book not found.")
        else:
            # If book found, rewrite the file excluding the book to be removed
            self.file.seek(0)
            self.file.truncate()
            for book in updated_books:
                self.file.write(book)
            print("Book removed successfully.")


# Creating object named "lib" with Library class
lib = Library()

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice.lower() == "q":
        # Quit the program if 'q' is entered
        break
    else:
        # Handle invalid input
        print("Invalid choice. Please try again.")

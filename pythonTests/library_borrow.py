from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies
        self.borrowed_by = {}  # member_id: due_date

    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies}/{self.total_copies} available)"

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []  # list of book titles

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

class Library:
    def __init__(self):
        self.books = {}  # title: Book object
        self.members = {}  # member_id: Member object
        self.loan_period = 14  # days

    def add_book(self, title, author, copies):
        self.books[title] = Book(title, author, copies)
        print(f"Added book: {title}")

    def add_member(self, member_id, name, email):
        self.members[member_id] = Member(member_id, name, email)
        print(f"Registered member: {name}")

    def borrow_book(self, member_id, book_title):
        if member_id not in self.members:
            return "Member not found!"
        if book_title not in self.books:
            return "Book not found!"

        book = self.books[book_title]
        member = self.members[member_id]

        if book.available_copies <= 0:
            return "No copies available!"
        if book_title in member.borrowed_books:
            return "Member already has this book!"

        book.available_copies -= 1
        member.borrowed_books.append(book_title)
        due_date = datetime.now() + timedelta(days=self.loan_period)
        book.borrowed_by[member_id] = due_date

        return f"Book borrowed successfully! Due date: {due_date.strftime('%Y-%m-%d')}"

    def return_book(self, member_id, book_title):
        if member_id not in self.members:
            return "Member not found!"
        if book_title not in self.books:
            return "Book not found!"

        book = self.books[book_title]
        member = self.members[member_id]

        if book_title not in member.borrowed_books:
            return "Member hasn't borrowed this book!"

        book.available_copies += 1
        member.borrowed_books.remove(book_title)
        del book.borrowed_by[member_id]

        return "Book returned successfully!"

    def display_status(self):
        print("\n=== Library Status ===")
        print("\nBooks in Library:")
        for book in self.books.values():
            print(book)

        print("\nBorrowed Books:")
        for book in self.books.values():
            if book.borrowed_by:
                for member_id, due_date in book.borrowed_by.items():
                    member = self.members[member_id]
                    print(f"'{book.title}' borrowed by {member.name} - Due: {due_date.strftime('%Y-%m-%d')}")

# Example usage
def main():
    library = Library()

    # Add books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 3)
    library.add_book("To Kill a Mockingbird", "Harper Lee", 2)
    library.add_book("1984", "George Orwell", 4)

    # Register members
    library.add_member("M001", "John Doe", "john@example.com")
    library.add_member("M002", "Jane Smith", "jane@example.com")

    # Process borrowings
    print("\n=== Processing Borrowings ===")
    print(library.borrow_book("M001", "The Great Gatsby"))
    print(library.borrow_book("M002", "1984"))
    print(library.borrow_book("M001", "To Kill a Mockingbird"))

    # Display current status
    library.display_status()

    # Process a return
    print("\n=== Processing Returns ===")
    print(library.return_book("M001", "The Great Gatsby"))

    # Display updated status
    library.display_status()

if __name__ == "__main__":
    main()
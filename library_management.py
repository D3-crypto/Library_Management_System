class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_book = []

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def add_book(self, book):
        self.books[book.book_id] = book
    
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book Removed")
        else:
            print("Book Not Found")
    
    def add_member(self, member):
        self.members[member.member_id] = member
    
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print("Member Removed")
        else:
            print("Member Not Found")
    
    def issue_book(self, book_id, member_id):
        if book_id in self.books and member_id in self.members:
            book = self.books[book_id]
            member = self.members[member_id]
            if book.copies > 0:
                book.copies -= 1
                member.borrowed_book.append(book_id)
                print(f"Book '{book.title}' issued to {member.name}")
            else:
                print("No copies available")
        else:
            print("Book or Member Not Found")
    
    def return_book(self, book_id, member_id):
        if book_id in self.books and member_id in self.members:
            book = self.books[book_id]
            member = self.members[member_id]
            if book_id in member.borrowed_book:
                book.copies += 1
                member.borrowed_book.remove(book_id)
                print(f"Book '{book.title}' returned by {member.name}")
            else:
                print("Book Not Borrowed")
        else:
            print("Book or Member Not Found")

    def search_books_by_title(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if not results:
            print("No books found.")
        return results
    
    def view_all_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books.values():
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Copies: {book.copies}")

    def view_borrowed_books(self, member_id):
        if member_id in self.members:
            member = self.members[member_id]
            for book_id in member.borrowed_book:
                book = self.books[book_id]
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        else:
            print("Invalid Member ID.")
        
    def view_all_members(self):
        for member in self.members.values():
            print(f"ID: {member.member_id}, Name: {member.name}")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book by Title")
        print("4. View All Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Add Member")
        print("8. Remove Member")
        print("9. View All Members")
        print("10. View Borrowed Books by Member")
        print("11. Exit")

        user_choice = input("Enter Your Choice: ")

        if user_choice == '1':
            book_id = input("Book ID: ")
            title = input("Book Title: ")
            author = input("Book Author: ")
            copies = int(input("Number of Copies: "))
            library.add_book(Book(book_id, title, author, copies))
            print("Book Added Successfully...")
    
        elif user_choice == '2':
            book_id = input("Book ID: ")
            library.remove_book(book_id)
    
        elif user_choice == '3':
            title = input("Book Title: ")
            results = library.search_books_by_title(title)
            if results:
                for book in results:
                    print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Copies: {book.copies}")
            else:
                print("No Books Found...")
    
        elif user_choice == '4':
            library.view_all_books()
    
        elif user_choice == '5':
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            library.issue_book(book_id, member_id)
    
        elif user_choice == '6':
            book_id = input("Enter Book ID: ")
            member_id = input("Member ID: ")
            library.return_book(book_id, member_id)
    
        elif user_choice == '7':
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(Member(member_id, name))
            print("Member Added Successfully...")
    
        elif user_choice == '8':
            member_id = input("Member ID: ")
            library.remove_member(member_id)
    
        elif user_choice == '9':
            library.view_all_members()

        elif user_choice == '10':
            member_id = input("Enter Member ID: ")
            library.view_borrowed_books(member_id)
    
        elif user_choice == "11":
            print("Thank you for using Library Management System")
            break

if __name__ == "__main__":
    main()

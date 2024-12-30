from dbm.ndbm import library
import book
import library
import borrower

#Create books
book1 = book.Book("The Great Gatsby", "F, Scott Fitzgerald")
book2 = book.Book("1983", "George Orwell")

#add books to library
lib = library.Library()
lib.add_book(book1)
lib.add_book(book2)

print("Initial books in the library:")
for b in lib.inventory:
    print("- " + b.title)

#create borrowers
john = borrower.Borrower("John Doe")
jane = borrower.Borrower("Jane Smith")

print("\nJohn tries to borrow 'The Great Gatsby'...")
lib.checkout_book(book1, john)

print("\nJane tries to borrow 'The Great Gatsby'...")
lib.checkout_book(book1, jane)

print("\nBooks John has borrowed:")
for b in john.borrowed_books:
    print("- " + b.title)

print("\nAvailable books in the library:")
print(lib.list_available_books())

print("\nJane tries to return 'The Great Gatsby'...")
lib.return_book(book1, jane)

print("\nJohn returns 'The Great Gatsby'...")
lib.return_book(book1, john)

print("\nJane tries again to borrow 'The Great Gatsby'...")
lib.checkout_book(book1, jane)

print("\nBooks Jane has borrowed:")
for b in jane.borrowed_books:
    print("- " + b.title)

print("\nCurrent available books in the library:")
print(lib.list_available_books())
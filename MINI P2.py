# book_set=set()
# book_list=[]
# issued_books={}
# def add_book():
#     name=input("Enter book name: ")
#     author=input("Enter author name: ")
#     if name in book_set:
#         print("Book already present")
#     else:
#         book_list.append((name,author))
#         book_set.add(name)
#         print("book added successfully")
# def issue_book():
#     if len(book_list) == 0:
#         print("No books available")
#         return
#     for i in range(len(book_list)):
#         print(i + 1, book_list[i][0], "by", book_list[i][1])
#     choice=int(input("Enter book number to issue_book: "))
#     book = book_list[choice]
#     book = book_list[choice]
#     if book[0] in issued_books:
#         print("Book already issued!")  # <-- sahi
#     else:
#         person = input("Enter your name: ").strip()
#         issued_books[book[0]] = person  # <-- change: save in dict
#         print(f"Book '{book[0]}' issued to {person}")  # <-- sahi
#
#
# def show_books():
#     print(book_list)
# while True:
#     print("1. Add Book")
#     print("2. Issue Book")
#     print("3. Show Available Books")
#     print("4. Exit")
#     choice = input("Enter choice: ").strip()
#
#     if choice == "1":
#         add_book()
#     elif choice == "2":
#         issue_book()
#     elif choice == "3":
#         show_books()
#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice! Try again.")
#
#

# working code


# book_set = set()
# book_list = []
# issued_books = {}
#
#
# def add_book():
#     name = input("Enter book name: ")
#     author = input("Enter author name: ")
#     if name in book_set:
#         print("Book already present")
#     else:
#         # CHANGE: store as tuple (name, author) instead of just name
#         book_list.append((name, author))  # <-- yahan change
#         book_set.add(name)
#         print("book added successfully")
#
#
# def issue_book():
#     if len(book_list) == 0:
#         print("No books available")
#         return
#
#     # CHANGE: print book properly with index
#     for i in range(len(book_list)):
#         print(i + 1, book_list[i][0], "by", book_list[i][1])  # <-- sahi
#
#     # CHANGE: indentation fix, input should be inside function
#     choice = int(input("Enter book number to issue: ")) - 1  # <-- -1 for index
#
#     # CHANGE: proper check for issued books
#     if choice < 0 or choice >= len(book_list):
#         print("Invalid choice")
#         return
#
#     book = book_list[choice]
#     if book[0] in issued_books:
#         print("Book already issued!")  # <-- sahi
#     else:
#         person = input("Enter your name: ").strip()
#         issued_books[book[0]] = person  # <-- change: save in dict
#         print(f"Book '{book[0]}' issued to {person}")  # <-- sahi
#
#
# def show_books():
#     # CHANGE: show books with status instead of raw list
#     if len(book_list) == 0:
#         print("No books available")
#     else:
#         for book in book_list:
#             status = "Issued" if book[0] in issued_books else "Available"
#             print(f"{book[0]} by {book[1]} ({status})")  # <-- change
#
#
# while True:
#     print("1. Add Book")
#     print("2. Issue Book")
#     print("3. Show Available Books")
#     print("4. Exit")
#     choice = input("Enter choice: ").strip()
#
#     if choice == "1":
#         add_book()
#     elif choice == "2":
#         issue_book()
#     elif choice == "3":
#         show_books()
#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice! Try again.")


# class Library:
#     def __init__(self):
#         self.book=[]
#         self.issued_book=[]
#     def show_book(self):
#         if len(self.book)==0:
#             print("no book available in library")
#         else:
#             print("book available in library")
#             for i in self.book:
#                 print(i)
#     def add_book(self,book_name):
#         for i in book_name.split(","):
#             self.book.append(i)
#         print("added book",book_name)
#
#     def remove_book(self,book_name):
#         if book_name in self.book:
#             self.book.remove(book_name)
#             print(book_name,"removed from library")
#         else:
#             print("book does not exist in library")
#     def search_book(self,book_name):
#         if book_name in self.book:
#             print(book_name,"found in library")
#         elif book_name in self.issued_book:
#             print(book_name,"currently issued")
#         else:
#             print("book does not exist in library")
#     def issue_book(self,book_name):
#         if book_name in self.book:
#             self.book.remove(book_name)
#             self.issued_book.append(book_name)
#             print(book_name,"issued")
#         else:
#             print("book does not exist in library already issued")
#     def return_book(self,book_name):
#         if book_name in self.issued_book:
#             self.issued_book.remove(book_name)
#             self.book.append(book_name)
#             print(book_name,"returned")
#         else:
#             print("book not issued")
#
# library = Library()
# while True:
#     print("\n---- Library Management System ----")
#     print("1. Show available books")
#     print("2. Add book")
#     print("3. Remove book")
#     print("4. Search book")
#     print("5. Issue book")
#     print("6. Return book")
#     print("7. Exit")
#     choice=input("Enter your choice: ")
#     if choice=="1":
#         library.show_book()
#     elif choice=="2":
#         book=input("Enter book name: ")
#         library.add_book(book)
#     elif choice=="3":
#         book=input("Enter book name: ")
#         library.remove_book(book)
#     elif choice=="4":
#         book=input("Enter book name: ")
#         library.search_book(book)
#     elif choice=="5":
#         book=input("Enter book name: ")
#         library.issue_book(book)
#     elif choice=="6":
#         book=input("Enter book name: ")
#         library.return_book(book)
#     elif choice=="7":
#         print("Thank you for using this library")
#         break
#     else:
#         print("invalid choice")














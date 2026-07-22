# Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created
class Book:
    total=0
    def __init__(self,t,A):
        self.title=t
        self.Author=A
        Book.total+=1
    @staticmethod
    def is_valid(t):
        return len(t)>3
    @classmethod
    def from_string(cls,book_str):
        t,A=book_str.split("-")
        if cls.is_valid(t):
            b=Book(t,A)
            return b
        else:
            print("Invalid Title")
b1=Book.from_string("classmate-Idris")
if b1:
    print(b1.title,b1.Author,sep="\n")
else:
    print("nothing in the object")
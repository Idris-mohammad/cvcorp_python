class Book:
    total_books=0
    def __init__(self,n,A):
        self.Name=n
        self.Author=A
        Book.total_books+=1
    @classmethod
    def creation(cls,n,A):
        if len(n)>=5:
            return cls(n,A)
        else:
            print("Title is too short")
    @classmethod
    def update(cls,nt):
        cls.total_books=nt
        print(f"total_books:{cls.total_books}")
b1=Book.creation("The Author's Pov","Author")
b1.update(30)
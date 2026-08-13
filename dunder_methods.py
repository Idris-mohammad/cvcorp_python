# 1.__str__ and __repr__
# Create a class Book with attributes title, author, and price.
# Define __str__ to return: 'Title by Author — Rs.Price' and __repr__ to return: "Book('Title', 'Author', Price)".
# Verify both using print(), repr(), and in an f-string.
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def __str__(self):
        return f"{self.title} by {self.author} - Rs.{self.price}"
    def __repr__(self):
        return f"Book({self.title},{self.author},{self.price})"
b1=Book("classmate","Idris",4)
print(b1)
print(repr(b1))

# 2 Arithmetic Dunders
# Write a class Vector2D(x, y).
# Implement __add__, __sub__, __mul__ (scalar multiply), __truediv__ (scalar divide), __floordiv__, and __mod__ (element-wise).
# Also add __str__ and __repr__.
# Test: Vector2D(3,4) + Vector2D(1,2) should give Vector2D(4,6).
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Vector2D(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Vector2D(self.x-other.x,self.y-other.y)
    def __mul__(self, other):
        return Vector2D(self.x*other.x,self.y*other.y)
    def __truediv__(self, other):
        return Vector2D(self.x/other.x,self.y/other.y)
    def __floordiv__(self, other):
        return Vector2D(self.x//other.x,self.y//other.y)
    def __mod__(self, other):
        return Vector2D(self.x%other.x,self.y%other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"({self.x},{self.y})"
v1=Vector2D(3,4)
v2=Vector2D(1,2)
print(v1)
print(v2)
print(v1+v2)
print(v1*v2)
print(v1-v2)
print(v1/v2)
print(v1//v2)
print(v1%v2)

# 3 Relational Dunders
# Create a class Temperature(celsius).
# Implement all six relational dunders (__lt__, __le__, __gt__, __ge__, __eq__, __hash__).
# Sort a list of Temperature objects and store them in a set.
# Verify: Temperature(100) > Temperature(50) is True.
class Temperature:
  def __init__(self, celsius):
    self.celsius = celsius
  def __lt__(self, other):
    return self.celsius < other.celsius
  def __le__(self, other):
    return self.celsius <= other.celsius
  def __gt__(self, other):
    return self.celsius > other.celsius
  def __ge__(self, other):
    return self.celsius >= other.celsius
  def __eq__(self, other):
    return isinstance(other, Temperature) and self.celsius == other.celsius
  def __hash__(self):
    return hash(self.celsius)
  def __repr__(self):
    return f'Temperature({self.celsius})'
print(Temperature(100) > Temperature(50))
temps_list = [Temperature(30), Temperature(10), Temperature(20)]
sorted_temps = sorted(temps_list)
print('Sorted:', sorted_temps)
temps_set = {Temperature(100), Temperature(50), Temperature(100)}
print('Set:', temps_set)

# 4 __len__ and __contains__
# Build a class Library with a list of book titles.
# Implement __len__ (number of books), __contains__ (check if a title is in the library), and __str__ (returns 'Library with N books').
# Test all three methods including bool() on an empty library.
class Library:
    def __init__(self):
        self.book_titles = []
    def __len__(self):
        return len(self.book_titles)
    def __contains__(self, title):
        return title in self.book_titles
    def __str__(self):
        return f"Library({self.book_titles})"
    def bool(self):
        return False if self.book_titles else True
l1=Library([""])
print(l1)
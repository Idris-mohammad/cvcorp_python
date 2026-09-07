class Animal:
    def make_sound():
        print("Making sound")
class Dog(Animal):
    def make_sound():
        print("Dog Making sound")
class Cat(Animal):
    def make_sound():
        print("Cat Making sound")
class Cow(Animal):
    def make_sound():
        print("Cow Making sound")
l=[Dog,Cat,Cow]
for i in l:
    i.make_sound()
# Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.
class Student:
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def is_passed(self):
        if self.marks>40:
            return True
        else:
            return False
s1=Student("kunal",68)
s2=Student("kamra",33)
print(s1.is_passed())
print(s2.is_passed())

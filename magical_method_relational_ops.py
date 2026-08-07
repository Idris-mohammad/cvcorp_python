class Student:
    def __init__(self,i,n,m):
        self.name=n
        self.marks=m
        self.Id=i
    def __gt__(self,other):
        return self.marks>other.marks
    def __lt__(self,other):
        return self.marks<other.marks
    def __eq__(self,other):
        return self.marks==other.marks
    def __hash__(self):
        return hash(self.Id)
    def __repr__(self):
        return self.name
s1=Student(25,"sai",100)
s2=Student(10,"suresh",100)
s3=Student(1,"mahesh",100)
s={s1,s2,s3}
print(s)
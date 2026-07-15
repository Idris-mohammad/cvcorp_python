class Students:
    Batch='PY-16'
    total=0
    def __init__(self,N,A,B):
        self.Name=N
        self.Age=A
        self.Branch=B
        Students.total+=1
s1=Students("Madara",47,"CSE")
s2=Students("Itachi",30,"ECE")
print(s1.Name,s2.Age)
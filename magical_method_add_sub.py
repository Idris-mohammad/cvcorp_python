class Vector:
    def __init__(self,a,b):
        self.num=a
        self.num2=b
    def __add__(self, o2):
        return self.num+o2.num,self.num2+o2.num2
    def __sub__(self, o2):
        return self.num-o2.num,self.num-o2.num2
    def __str__(self):
        return f"vector({self.num,self.num2})"
    def __repr__(self):
        return f"vector({self.num,self.num2})"
v1=Vector(7,8)
v2=Vector(6,7)
v3=Vector(3,4)
print(v1+v2+v3)
v4=v1+v2+v3
print(v4)
# print(v1+v2)
# print(v1-v2)
# print(v1)
# l=[v1,v2]
# print(l)
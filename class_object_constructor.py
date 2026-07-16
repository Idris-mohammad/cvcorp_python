class Car:
    fuel_type='Petrol'
    def __init__(self,mak,m,y,p):
        self.make=mak
        self.model=m
        self.year=y
        self.price=p
    def display(self):
        print(self.make,self.model,self.year,self.price)
c1=Car("Tata","Punch",2024,150000)
c2=Car("Mahindra","SUV",2018,100000)
c1.display()
c2.display()
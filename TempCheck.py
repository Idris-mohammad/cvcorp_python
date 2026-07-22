# Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.
class Temperature:
    def __init__(self,c):
        self.celsius=c
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5)+32
    def show_conversion(self):
        fahrenheit=Temperature.to_fahrenheit(self.celsius)
        print("Celsius:",self.celsius)
        print("Fahrenheit:",fahrenheit)
t=Temperature(25)
t.show_conversion()
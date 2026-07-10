from cvcorp_python_section4 import question_no

def power(base,exponent=2):
    return base**exponent
def connect(host,port=3306,protocol='TCP'):
    return f"{host}\n{port}\n{protocol}"
if question_no==5:
    print(connect("windows"))
    print(connect("linux",1103,'UDP'))
    print(connect("mac",1202,'SMTP'))
elif question_no==6:
    print(f"with 1 argument:{power(10)}\nwith 2 arguments:{power(10,3)}")
else:
    print("Invalid input")
    '''def func(name='guest',age):
        return name,age
    print(func("uriya",19))'''
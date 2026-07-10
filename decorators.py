def register(func):
    uns=[]
    def inner(us:str,psd:str,age):
        sp=['@','#','!','$','%','&','_']
        if len(psd)>=8:
            up=list(filter(lambda x:x.isupper(),psd))
            sc=list(filter(lambda x:x in sp,psd))
            dg=list(filter(lambda x:x.isdigit(),psd))

            if up and sc and dg:
                print("Strong Password")
                func(psd)
            else:
                print("Weak Password")
        else:
            print("password must contain 8 characters")
        if age>=18:
            func(us,psd,age)
        else:
            print("Age must be 18 above")
    return inner
@register
def registration(us,psd,age):
    print(f"username:{us}\npassword:{psd}\nage:{age}")
registration()
while True:
    def send_email(to,subject,body):
        return f"To: {to}\nSubject:{subject}\nBody:{body}"
    res=send_email(body="hi",subject="chat",to="madara")
    def create_profile(username,email,age):
        return f"Username:{username}\nEmail:{email}\nAge:{age}"
    def error_check(a,b):
        return a,b
    def book_ticket(name,destination,start,passengers):
        return f"Name:{name}\nDestination:{destination}\nFrom:{start}\nPassengers:{passengers}"
    question_no=int(input("enter question no(1-4):"))
    if question_no==4:
        print(book_ticket(name="Alice",passengers=2,start="Mumbai",destination="Delhi"))
        print("-----------------------------------------------------------------------")
    elif question_no==2:
        print(create_profile(age="106",username="tsunade",email="tsunade106@gmail.com"))
        print("-----------------------------------------------------------------------")
    elif question_no==1:
        print(res)
        print("-----------------------------------------------------------------------")
    else:
        break
# Write a function multiply_all(*args) that returns the product of all numbers passed.
#     Q2.  Create a function display_tags(**kwargs) that prints each keyword-value pair on its
#     own line.
#     Q3.  Write a function describe_person(name, *hobbies) where name is a regular param and
#     hobbies are collected into a tuple.
#     Q4.  What is the output of: def f(*args): print(type(args))  →  f(1, 2, 3)? Explain why.
#     Q5.  Write a function create_html_tag(tag, **attributes) that prints: <tag key='val' ...>.
#     Example: create_html_tag('a', href='https://python.org', target='_blank')
# Q6.  Write a function mixed(a, b, *args, **kwargs) and call it with at least 6 arguments. Print
# each part.
while True:
    def multiply_all(*args):
        prod=1
        for i in range(len(args)):
            prod*=args[i]
        return prod
    def display_tags(**kwargs):
        for key,value in kwargs.items():
            print(f"{key}:{value}")
    def describe_person(name,*hobbies):
        return f"my name is {name}\nmy hobbies are {hobbies}"
    def f(*args):
        print(type(args))
    def create_html_tag(tag,**attributes):
        print(f"<{tag }{attributes}>")
    def mixed(a,b,*args,**kwargs):
        print(f"{a} {b}\n{args}\n{kwargs}")
    Q_no=int(input("enter_question number(1-6): "))
    if Q_no==6:
        mixed(1,2,60,80,g=20,y=78)
        print("-----------------------------------")
    elif Q_no==5:
        create_html_tag('a',href='https://python.org',target='_blank')
        print("-----------------------------------")
    elif Q_no==4:
        f(1,2,3)
        print("-----------------------------------")
    elif Q_no==3:
        print(describe_person("Idris","cricket","chess","puzzles","movies"))
        print("-----------------------------------")
    elif Q_no==2:
        display_tags(a=1,b='a',c='d')
        print("-----------------------------------")
    elif Q_no==1:
        print(multiply_all(1,2,3,4,5))
        print("-----------------------------------")
    else:
        break


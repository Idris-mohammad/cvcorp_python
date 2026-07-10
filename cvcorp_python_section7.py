# Practice Questions — Section 7: Functional References
# Q1.  Assign the built-in function len to a variable called count. Use it to find the length of a
# list.
# Q2.  Write a function run_twice(func, value) that calls func on value twice and returns the
# final result.
# Q3.  Store the functions upper, lower, and title (string methods) in a dictionary. Let the user
# choose which one to apply.
# Q4.  Write a function that returns another function. Example: make_multiplier(3) should
# return a function that multiplies any number by 3.
# Q5.  Can you store the same function under multiple names in a dictionary? Test it and
# explain what happens.
l=[1,2,3,4]
length=len(l)
def run_twice(func,value):
    return func(value)
def two_times(x):
    return x*2
def square(x):
    return x*x
q_num=int(input())
if q_num==2:
    print(run_twice(two_times,9),run_twice(square,9))
    print(length)

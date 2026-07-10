from functools import reduce
#  Given two lists:
# a = [1, 2, 3, 4] b = [10, 20, 30, 40]
# Use map() with a lambda to create a new list containing the sum of corresponding
# elements.
a = [1, 2, 3, 4]
b = [10, 20, 30]
m=list(map(lambda x,y:x+y,a,b))
print(m)
#  Given a list:
# nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
# 5 but NOT divisible by both.
nums = [12, 15, 7, 18, 20, 21, 25]
n=list(filter(lambda x:x%3==0 or x%5==0,nums))
print(n)
# Given a list:
# nums = [1, 2, 3, 4]
# Use reduce() with a lambda to compute the sum, but start with an initial value
# of 10
numbers = [1, 2, 3, 4]
o=reduce(lambda x,y:x+y,numbers,10)
print(o)
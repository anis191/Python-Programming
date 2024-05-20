# range(): Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
range(0,5) # --> (0,1,2,3,4)
range(3,6) # --> (3,4,5)
# for loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# Syntax --> for variable in list:
# print 1-5 using for loop:-
numbers = [1,2,3,4,5]
print("numbers list print start:-")
for i in numbers:
    print(i)
name = ['anis','muhi','shariar']
print("name list print start:-")
for n in name:
    print(n)
tuple = ('anis',2314,True)
print("tuple print start:-")
for k in tuple:
    print(k)
set = {5,60,'hello'}
print("set print start:-")
for s in set:
    print(s)
for f in range(3,9): #range(1st_value,last_value)--> here 1st_value is starting value and last value is ending value(last_value-1)
    print(f)
# range() Syntax -->
# 1. when 2 value parameter: range(first_value,last value) -->
# here, first value is the starting value, and last value is the ending value
# 2. when 3 value parameter: range(fist_value,last_value,increment)
# here, extra increment value is increment the loop variable
x = range(3,19,2) # it meanse 3 to 18(19-1)
for d in x:  # when loop is runing,it increment/go forword 2 times
    print(d," ",end='')

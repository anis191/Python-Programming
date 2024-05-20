# Recursion Syntax -->
'''
def function_name(parameters...):
    Base Case()
    //code statements
    function_name(inputs...) --> it's call "recursive call"
'''
# print 1 to n using recursion(do not use loop)?
def print_number(n,i):
    if i > n:
        return
    print(i)
    return print_number(n, i+1)
n = int(input())
print_number(n,1)
# factorial using recursion?
def fact(n,sum):
    if n < 1:
        return sum
    sum *= n
    return fact(n-1,sum)
n = int(input())
ans = fact(n,1)
print(ans)
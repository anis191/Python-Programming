# A block of code
# Syntax -->
'''
def function_name(parameters,....):
    //code/statements
    return ___
'''
# When we need to run/execute a function, we should need to call that function:
'''
function call syntax -->
    function_name(input1,input2....)
'''
# A function which is return sum/sub,mul,div,mod of two nuymbers-->
def calculation(a,b):
    print("select operation(+,-,*,/,%): ",end='')
    operator = input()
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    else:
        return a%b
a = int(input("Enter a: "))
b = int(input("Enter b: "))
ans = calculation(a,b)
print(ans)
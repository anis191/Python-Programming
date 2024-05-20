#Develop a Python script that simulates a basic calculator with options for addition, subtraction, multiplication, and division. The program should continue running until the user chooses to exit.
s = input("choose operator(+,-,*,/,%,**): ")
if s=='+'or s=='-'or s=='*'or s=='/'or s=='%'or s=='**':
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    if s=='+':
        print(a,"+",b,"=",a+b)
    elif s=='-':
        print(a,"-",b,"=",a-b)
    elif s=='*':
        print(a,"*",b,"=",a*b)
    elif s=='/':
        print(a,"/",b,"=",a/b)
    elif s=='%':
        print(a,"%",b,"=",a%b)
    else:
        print(a,"**",b,"=",a**b)
else:
    print("Enter Valid operators")
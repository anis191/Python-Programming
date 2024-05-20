#Write a Python script that calculates the factorial of a given integer using a while loop.
n = int(input("Enter an integer number: "))
ans = 1
i = n
while i>=1:
    ans *= i
    i -= 1
print("Factorial of",n,"is: ",ans)
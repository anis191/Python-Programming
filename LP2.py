#Write a Python program to find the largest number in a list.Where take input from users
#also find the sum of all elements in a list.
n = int(input("Enter list size: "))
numbers=[] #Empty/null list
list_sum = 0 #For store sum of all list elements
i=0
while i<n:
    x = int(input())
    numbers.append(x)
    list_sum += numbers[i] #this line is for calculate all list value sum
    i +=1
max = numbers[0]
i=1
while i<n:
    if max < numbers[i]:
        max = numbers[i]
    i +=1
print("Large number is: ",max)
print("Sum is: ",list_sum)
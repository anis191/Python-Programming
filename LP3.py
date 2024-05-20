#Write a Python program to remove duplicates from a list.
n=int(input("Enter list size: "))
list=[]
i=0
while i<n:
    x=input()
    list.append(x)
    i +=1
Unique_list=[]
i=0
while i<n-1:
    j=i+1
    while j<n:
        if list[i] == list[j]:
            continue;
        else:
            Unique_list.append(list[i])
        j +=1
    i +=1
print(Unique_list)
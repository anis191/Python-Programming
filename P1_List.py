#Syntax of List build-in data type:-
# List_Name = [item1,item2,item3,.....item_n]
marks = [90,45,45,78,80,90] #allow duplicate values(items)
print(marks)
j = 100
i=len(marks)-1
while i>=0:
    marks[i] = j; # Changeable
    print(marks[i]," ",end='') #orderd(have index)
    j = j-30
    i -=1
# Length of a list syntax:-
# use len() function--> len(list_name)
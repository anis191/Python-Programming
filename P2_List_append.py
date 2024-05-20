# append(): Adds an element at the end of the list
# Syntax --> list.append(parameter)
# 1.Add a number item in a list:-
new = [1,2]
new.append(5)
print(new)
# 2.Add a string item in list:
new.append("Anisul Alam")
print(new)
# 3.Add a boolean item in list:
new.append(True)
print(new)
# 4.Add a list to another list:
my_self=["Hello",2314,3.30,False]
new.append(my_self)
print(new)
# For sure,now we see all item with it's dataType:
i=0
while i<len(new):
    print(new[i],type(new[i]))
    i +=1
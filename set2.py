# SET Methods:-
# 1.add():Adds an element to the set
# Syntax --> set_name.add(items)
info = set() #at first i will take a null/empty set
info.add('Anis') #now add a element in the set
print(info)
tuple = (2,'world')
info.add(tuple) #we can add a tuple in set.Because tuple and set both are unchangeable
print(info)
list = [1,'hello'] #now add this list on "info" set
info.add(list) # we can't add a list in set.Because list is changeable and set is unchangeable
print(info) #it show a error
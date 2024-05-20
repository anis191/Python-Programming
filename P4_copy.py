# copy(): Returns a copy of the list(It copy a full list in another list)
# Syntax --> new_list = old_list.copy()
list_a = ['apple','banana',2314,False]
list_b = list_a.copy() #copy() method will copy the list(list_a),and store it in another list(list_a)
print(list_a)
print(list_b)
# count(): Return the number of times a item appears in the list:
# Syntax --> x = list.count(item)
''' Here this(count()) method return a integer number,which is a value of that item how many times
appeats in the list.'''
numbers=[0,3,4,5,7,1,34,0,2,3,4,6,7,4,4,5,6,4] #Here "4" appears 5 times
a = numbers.count(4) #count() method will count the item(4) how many times appears in the list, and store it in "a"
print(a) #It show output-5
frutis=['mango','banana','mango','pinapple','mango'] #Here "mango' appears 3 times
b = frutis.count('mango') #count() method will count the item('mango') how many times appears in the list, and store it in "b"
print(b) ##It show output-3
# index(): Returns the index number of an specified item/element in the list(index first time founded).
# Syntax --> x = list.index(item)
c = numbers.index(34) #index() method will search the item(34) in list.When it find first time,it return it's index number and store it in "c"
print(c)
d = frutis.index('mango')
print(d)
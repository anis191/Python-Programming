#A tuple is a collection of data which is ordered and unchangeable
# Syntax1 --> tuple_name=(item1,item2,......item_n)
# Syntax2 --> tuple_name=tuple((item1,item2,....item_n))
numbers = (1,5,6,8,10)
print(numbers)
print(type(numbers))
my_self = ("Aniul Alam",2314,5.00,True)
print(my_self)
i=0
while i<len(my_self):
    print(my_self[i],type(my_self[i]))
    i +=1
#Tuple Methods:-
#count(): Returns the number of times a specified value occurs in a tuple
name = ('anis','muhi','rahim','anis','karim','anis','muhi')
x = name.count('anis') # 'anis' is 3 times occurs in the tuple
y = name.count('muhi') # 'muhi' is 2 times occurs in the tuple
print(x,y)
#index(): Searches the tuple for a specified value and returns the position of where it was found
a = name.index('anis')
b = name.index('muhi')
print(a,b)
# tupe can store a whole list/another tuple etc. like list:
list=['hello',2,'world']
new = (1,2,3,name,list)
print(new)
list.append(name)
print(list)
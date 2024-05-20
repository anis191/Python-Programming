# clear(): Removes all the elements from the list
# Syntax --> list.clear()
student = ["Anis",2314,4.00,True]
print(student)
student.clear() #remove all items from student-list
print(student) #Now all are removed(show empty)
student2 = ["Muhi",2314,4.00,True] #A new list
std = ["Hi",10,False] #Another new list
student2.append(std) #add std-list in student2-list
print(student2)
std.clear() #remove all item from std-list
print(student2) #Show student2-list full,but included std-list are empty
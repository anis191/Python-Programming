# First of all we need to open a file for read,write,modify etc.
# File open Syntax -->
'''
object_variable = open("file_name/file_path","mode")
explanation:-
object_variable --> Here the file is temporary stored, for our working porpose
open() --> This is the "open()" function for open a file
file_name/file_path --> "demo.txt" or "/user/desktop/hp/demo.txt"
mode --> "r" , "w", "a", "r+" , "w+" etc.
'''
print("demo.txt file open -->")
f = open("demo.txt","rt")
data1 = f.read() # It can read all data from file. Read whole file
print(data1)
f.close()
print("closed demo.txt file <--\n")

print("demo2.txt file open -->")
f2 = open("demo2.txt","rt")
data2 = f2.read(16) # We can read spacific numbers of values(characters) from file.
print(data2)
f2.close()
print("closed demo2.txt file <--\n")

print("demo3.txt file open -->")
f3 = open("demo3.txt","rt")
print(f3.readline(),end='') # 1st time readline() was read 1st line from file
print(f3.readline(),end='') # 2nd time readline() was read 2nd line from file
print(f3.readline()) # 3rd time readline() was read 3rd line from file
f3.close()
print("closed demo3.txt file <--")


a = open("C:\\Users\\HP\\Downloads\\FullDatabase\\bus_management_full_database.txt","r")
b = a.read()
#print(b)
a.close()

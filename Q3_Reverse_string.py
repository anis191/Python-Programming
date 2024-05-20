#Develop a Python script that reverses a given string using a while loop.
str = input("Write something: ")
l = len(str)
i = l-1
while i>=0:
    print(str[i],end='')
    i -= 1
# Here use (end='') for stop automatic print newline!
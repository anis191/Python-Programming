# With:-
# "With" is a format of file input_output all operation:
'''
Syntax -->
with open("file_name/path","mode") as variable:
    .read()
    .write("")
    //all code statements
**when we open a file using "with" syntax.After all work,it automatic close file.
'''
with open("demo7.txt","rt") as anis:
    print(anis.read())

#  Add something in demo7.txt :
with open("demo7.txt","at") as anis:
    anis.write("\nCity : Patia")

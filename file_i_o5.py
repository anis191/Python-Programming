# We can delete any file using "remove()" function.
# Fist of all we should import the library of "remove()" function.
# The library of "remove()" is --> OS
'''
file delete syntax -->
    import os
    os.remove("file_name/path")
'''
#new = open("file_for_delete.txt","xt") --> this line is just for create a empty file
import os
os.remove("file_for_delete.txt")
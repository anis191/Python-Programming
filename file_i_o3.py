'''
For write on a file, we have to use two mode("w" and "a"):
1. "a"- Append --> will append to the end of the file
2. "w"- Write --> will overwrite any existing content:
** Syntax--> .write("......")
'''
# Using "w"(overwrite) mode:-
k = open("demo5.txt","wt")
k.write("I am Anisul Alam!\nWho are you?")
k.close()

# Using "a"(append) mode:-
q = open("demo6.txt","at")
q.write("\nI am Anisul Alam\nWho are you?")
q.close()

# In "a"-mode,if opening name has no file exiest, than it create a file than write here!
p = open("demo_create_by_a_mode.txt","at")
p.write("Name : Anisul Alam\nId : 2314\nSemester : 6th")
p.close()

# Create a empty file(without writeing anything) --> mode: "x"
w = open("create_file_using_x_mode","xt") #It will create a empty file name-"create_file_using_x_mode"

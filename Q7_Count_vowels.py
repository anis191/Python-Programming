#Develop a program that counts the number of vowels in a given string entered by the user.
s = input("Write something:")
count = 0
i =0
while i<=len(s)-1:
    if s[i].lower()=='a' or s[i].lower()=='e' or s[i].lower()=='i' or s[i].lower()=='o' or s[i].lower()=='u':
        count +=1
    i +=1
print("Ans is: ",count)

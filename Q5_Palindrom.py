#Create a Python program that checks if a given string is a palindrome (reads the same forwards and backwards).
s = input("Write something: ")
j = len(s)-1
checker =0
i = 0
while i<len(s)-1:
    if s[i] != s[j]:
        checker += 1
        break
    else:
        i +=1
        j -=1
        continue
if checker != 0:
    print("Not palindrome")
else:
    print("palindrome")
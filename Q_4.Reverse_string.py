# #Write a program that asks the user to input their name and then prints it back in uppercase.
# str = input("Write Something: ")
# i = len(str) - 1
# while i>=0:
#     print(str[i].upper(),end='')
#     i -= 1
s = input()
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
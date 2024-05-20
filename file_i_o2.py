# f = open("demo4.txt","rt")
# for i in f:
#     print(i)
# f.close()

# print full file using readline -->
f2 = open("demo4.txt","rt")
for i in range(7):
    print(f2.readline())
f2.close
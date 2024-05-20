n = int(input())
temp = n
r = 0
while temp != 0:
    r = temp % 10
    temp = temp // 10
    print(r)

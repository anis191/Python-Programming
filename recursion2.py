def table(n,i):
    if i > 10:
        return
    print(n,"x",i,"=",(n*i))
    table(n,i+1)
n=int(input())
table(n,1)
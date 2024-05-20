# we can set a function parameter as default.

def func(a,b=3): 
    #here we take just parameter value for "a", set "b" is default "3"
    for i in range(b):
        print(i,'.',a)
a=input("Enter: ")
func(a)
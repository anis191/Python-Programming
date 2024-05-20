# We can pass any list,tuple,dict,set in a function as input-->
def all_in_list(string_1,list_1,tuple_1,set_1,dictionary):
    # We store all in the list-->
    list_1.append(string_1)
    list_1.append(tuple_1)
    list_1.append(set_1)
    list_1.append(dictionary)
    print(list_1,type(list_1))
    return
def all_in_tuple(string_1,list_1,tuple_1,set_1,dictionary):
    # We store all in a tuple(for that we need a new tuple)-->
    tuple_2=()
    tuple_2=(string_1,list_1,tuple_1,set_1,dictionary)
    print(tuple_2,type(tuple_2))
def all_in_set(string_1,list_1,tuple_1,set_1,dictionary):
    set_1.add(string_1)
    # set_1.add(list_1) --> This is wrong! because list items is changeable
    set_1.add(tuple_1)
    # set_1.add(dictionary) --> This is wrong! because dictionary items is changeable
    print(set_1)
def all_in_dict(string_1,list_1,tuple_1,set_1,dictionary):
    '''dictionary.update({'string':string_1},{'list':list_1},{'tuple':tuple_1})
    update expected at most 1 argument, got 3'''
    dictionary.update({'string':string_1})
    dictionary.update({'list':list_1})
    dictionary.update({'tuple':tuple_1})
    dictionary.update({'set':set_1})
    print(dictionary)
string_1 = "Hello World"
list_1 = [1,2,3]
tuple_1=('anis',2314)
set_1={1,2,3,'Start'}
dictionary={
    "name" : "robi",
    "id" : 2033,
    "gpa" :{
        "ssc" : 5.00,
        "hsc" : 3.00
    }
}
out = int(input("1.all_in_list\n2.all_in_tuple\n3.all_in_set\n4.all_in_dict: \n"))
if out == 1:
    all_in_list(string_1,list_1,tuple_1,set_1,dictionary)
elif out == 2:
    all_in_tuple(string_1,list_1,tuple_1,set_1,dictionary)
elif out == 3:
    all_in_set(string_1,list_1,tuple_1,set_1,dictionary)
else:
    all_in_dict(string_1,list_1,tuple_1,set_1,dictionary)
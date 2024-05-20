''' items(): Returns a list containing a tuple for each key value pair.
Means it return a list, which list items is tuples. And this every single tuple
is a tuple of (key:value) pair.
example:- dict_items([('key1','value1'),('key2','value2')...('key_n','value_n')])
    Suntax --> dictionary_name.items()
    Syntax(for nested dictionary) --> dictionary_name["keyword"].items()
'''
info = {
    "name" : "anis",
    "id" : 2314,
    "city" : "ctg",
    "result" :{
        "1st sem" : 2.00,
        "2nd sem" : 3.00,
        "3rd sem" : 2.50,
        "Advice" : "Never Give up"
    }
}
list = info.items()
print(list)
list_nested = info["result"].items()
print(list_nested)

# get(): Returns the value of a specified key
# Syntax --> dictionary_name.get("keyword")
# Syntax(for nested dictionary) --> dictionary_name["keyword"].get("keyword")
print(info.get("name"))
print(info.get("result"))
print(info["result"].get("3rd sem"))
# update(): We add a pair(key:value) of dictionary item/element using this method:
# Syntax --> dictionary_name.update({"keyword" : "value"})
# # Syntax -->(for nested dict.) dictionary_name["keyword"].update({"keyword" : "value"})
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
# we add this pair of data element --> university : PUC
info.update({"University" : "PUC","school":"PMHS"})
print(info)
info["result"].update({"hello" : "world"})
print(info)

# pop(): Removes a element(key:value) with the specified key
# Syntax --> dictionary_name.pop("keyword")
info.pop("city")
print(info)

# copy(): Returns a copy of the dictionary. It fully copy a dictionary
# Syntax --> new_dictionary = old_dictionary.copy()
new = info.copy()
print("data type of new is:",type(new))
print(new)

# clear(): Removes all the elements from the dictionary
# Syntax --> dictionary_name.clear()
info["result"].clear() # just remove all element from nested dictionary
print(info)
info.clear() # remove all elements from whole dictionary
print(info)
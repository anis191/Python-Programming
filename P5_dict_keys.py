#keys(): Returns a list all dictionary's keys
# Syntax --> dictionary_name.keys()
# Syntax(for nested dictionary) --> dictionary_name["keyword"].keys()
# {here keyword is nested dictionary name}
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
all_keys_of_info_dictionary = info.keys()
all_keys_of_info_nested_dictionary = info["result"].keys()
print(all_keys_of_info_dictionary)
print(all_keys_of_info_nested_dictionary)
# values(): Returns a list of all the values in the dictionary
# Syntax --> dictionary_name.values() {it also print/return it's own values and all nested dictionary values}
# Syntax(*just for nested dictionary) --> dictionary_name["keyword"].values()
print(info.values())
print(info["result"].values())
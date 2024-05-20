# Nested dictionary:-
'''
 Syntax -->
dictionary_name = {
    "keyword-1" : "value-1",
    "keyword-2": "value-2",
    ....................
    "keyword":{
        "keyword" : "value",
        "keyword2" : "value",
        ..................
    }
}
** Access nested dictionary value:-
Syntax --> dictionary_name["keyword"]["keyword"]
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
print(info)
print(info["result"])
# Change value of dictionary:-
info["city"] = "dhaka"
info["result"]["2nd sem"] = 100
print(info)
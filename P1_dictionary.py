#Dictionaries are used to store data values in key:value pairs.
# Syntax -->
'''
dictionary_name = {
    "keyword" : "value",
}
Here, keyword --> is a kind of variable("name"/"roll"/"city"...)which is store his value.
We can also use any number as keyword(1,2..)
values --> it's the main data which is we store in dictionary. dictionary can store all type of
data like(integer,float,char,string,list,tuple,set etc.)
'''
list=["apple","orange","multa","jackfood"]
tuple=("codeforces","hackerrank",'leetcode')
info = {
    "name" : "Anisul Alam",
    "id" : 2314,
    "GPA" : 4.50,
    "age" : 23,
    "Is_adult" : True,
    119 : "Favourite Number",
    "food" : list,
    "code" : tuple
}
print(info)
print(type(info))

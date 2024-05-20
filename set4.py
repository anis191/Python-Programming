# union(): Return a set containing the union of sets
# Syntax --> set1.union(set2)
set1 = {1,2,4,5,6,7,8}
set2 = {1,4,5,7,8,9,10}
set = set1.union(set2)
print(set)
# intersection(): Returns a set, that is the intersection of two other sets
set3 = {1,3,'anis',2314}
set4 = {'muhi',2234,3,'anis',0}
set5 = set3.intersection(set4)
print(set5)

# copy(): Returns a copy of the set
copy_set = set1.copy()
print(copy_set)

# If we entry duplicate value in set, it will auctomatic remove multiple value/items
test = {1,2,3,4,1,2,1,7}
print(test)
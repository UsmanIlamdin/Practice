'''
Map takes a function and a collection of items. 
It makes a new, empty collection, runs the 
function on each item in the original collection 
and inserts each return value into the new collection. 
It returns the new collection
'''
name_lengths = map(len, ["Mary", "Isla", "Sam"]) 
print(name_lengths)

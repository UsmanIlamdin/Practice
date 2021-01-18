from itertools import filterfalse
names = ['Fred', 'Wilma', 'Barney', 'usman' , 'arshad']
def lon_list(name):
    return len(name)> 5 
'''
filter taskes the function as input and all arguments
pass to that function and yields multiple items address
but can be convert into others data types
'''    
print(list(filter(lon_list , names)))


'''
filters without functions take None and single
argunment and return all true values
'''
names_list = ['' , None , ' ', 'ali' , 'haider']
print(list(filter(None , names_list)))


'''
filterfalse print the inverse 
if apply all meet that conditions dicards and
rest will be retunrs
'''
print(list(filterfalse(lon_list , names)))
print(list(filterfalse(None , names_list)))

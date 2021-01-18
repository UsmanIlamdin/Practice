x = [3, 1, 9] 
y = x # y is the argument, x is the parameter 
x.append(5) # Mutates the list labelled by x and y, both x and y are bound to [3, 1, 9]
x.sort() #Mutates the list labelled by x and y (in-place sorting) 
x = x + [4] # Does not mutate the list (makes a copy for x only, not y) 
z = x# z is x ([1, 3, 9, 4])
'''
this will be little confusing
and 
'''
x += [6] # Pretend that we wrote "x = y", then go to line 1 

# Mutates the list labelled by both x and z (uses the extend function).
x = sorted(x) # Does not mutate the list (makes a copy for x only). 
x
# Out: [1, 3, 4, 5, 6, 9] 
y
# Out: [1, 3, 5, 9] 
z

'''
inline operator is not creating new variable 
basically they are just adding and modifing same 
varaible
'''
X +=X-2

'''
On the other hand assignmnet operator first perform
task and then assign new varaible even if it will be
previous one new value varaible assign
'''

X = X+2


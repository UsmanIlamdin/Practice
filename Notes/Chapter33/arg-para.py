def foo(x):# here x is the parameter
    x[0] = 9 # This mutates the list labelled by both x and y 
    print(x)
y = [4, 5, 6]  # passing argument by assigning others variables
foo(y) # call foo with y as argument
# Out: [9, 5, 6] 
# list labelled by x has been mutated 
print(y)
#Out: [9, 5, 6] 
#list labelled by y has been mutated too
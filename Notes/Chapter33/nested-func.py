def makeInc(x): 
    def inc(y):
        return y + x 
    return inc
incOne = makeInc(1) 
incFive = makeInc(5)
print(incOne)
print(incFive)
print(incOne(5)) # returns 6 
print(incFive(5)) # returns 10

'''
Important Info
'''
'''
Notice that while in a regular closure the enclosed function 
fully inherits all variables from its enclosing environment, 
in this construct the enclosed function has only read access 
to the inherited variables but cannot make assignments to them
'''
def makeInc(x): 
    def inc(y): 
        x += y # incrementing x is not allowed
        return x
    return inc
incOne = makeInc(1) 
incOne(5) # this will return an error UnboundLocal varaible

'''
we can use nonlocal  to make assignment
'''
def makeInc(x): 
    def inc(y): 
        nonlocal x
        x += y # now assigning a value to x is allowed 
        return x
    return inc
incOne = makeInc(1) 
incOne(5) # returns 6

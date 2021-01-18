'''
Defining a function with an 
arbitrary number of arguments
'''

def test(*args):
    # this will taske n argunment as tuple
    for i in args:
        print(i , end='\t') # end by default is end = '\n'
        # but can be changed its behaviours

test(1,2,3,4,5,6,6)

list_argunment = ['ali' , 'hassan' , 'javeed']
def list_test(*list_argunment):
    for j in list_argunment:
        print(j)

print('\n')
print('\n')  
# how argument pass in function 
print(list_test(*list_argunment))
print('\n')
print('\n')

'''
Keyword argunment take dictionary key as argunment
'''

def func(**kwargs):
    #kwargs will be a dictionary containing the names as keys and the values as values 
    for name, value in kwargs.items(): 
        print(name, value)

# how keyword argument pass in function
func(value1=1, value2=2, value3=3) # Calling it with 3 arguments
func() # calling it without arguments
my_dict = {'foo': 1, 'bar': 2} # calling it with dic arguments
func(**my_dict)


'''
test default argument in function or class
'''
# Most import always default write after given argumnets
def func1(lis1 , name = 'Usman'):
    return None

print(func1.__defaults__)
'''
Decorators augment the behavior of other functions 
or methods. Any function that takes a function as a 
parameter and returns an augmented function can be 
used as a decorator.
'''

'''
decoretor help us add functionlaity to a function
'''
def hello():
    return 'Hello'
greet = hello
print(hello)
print(hello())
print(greet())
del hello
'''
print(hello())   return error base we delete hello word

the other thing is function are object thats why we pass the
object to another vairable
'''
print(greet())


'''
passing the function as an argument
'''

def pas(greet = 'hello world!'):
    return greet

def some_other(pas):
    print('Some maine function stuff')
    print(pas())

some_other(pas)

'''
this can be done using decoretors
decoretor in action
'''

def pas(greet = 'hello world!'):
    return greet
@pas
def some_other():
    print('Some maine function stuff')
    print(pas())
# this is equivalent to 
# some_other(pas)
some_other()


print('\n\n\n')

'''
deoretor in more complex way
'''
#This is the decorator 
def print_args(func): 
    def inner_func(*args, **kwargs): 
        print(args) 
        print(kwargs)
        return func(*args, **kwargs) #Call the original function with its arguments. 
    return inner_func
@print_args 
def multiply(num_a, num_b): 
    print('Do sum main function stuff')
    return num_a * num_b
print(multiply(3, 5))
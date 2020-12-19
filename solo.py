# print(list(range(5)))

# print(list(range(5, 10)))


# nums = list(range(3,15,3))

# for i in range(0, 20 , 2):
#     print(i)


# list = [1,2,3,4,5,6,7,8]
# print(list[list[4]])

# for i in range(10):
#   if not i % 2 == 0:
#     print(i+1)

# if len(list)%2 ==0:
#     print(list[0])


# for i in list:
#     print(i)

# '''
# DRY stand for don't repeat for yourself 
# must call function after it call
# must assign variable before call it
# one return something from function it stop the function and 
#     pointer to the place where it  start.

# '''

# def multiply(x , y):
#     return x*y

# operation = multiply

# print(operation(10, 20))


# #What is the output of this code?
# def shout(word):
#    return word * "!"

# speak = shout
# output = speak(2)
# print(output)
# output = speak('USMAN')
# print(output)


def add(x , y):
    return x + y

def twice(func , x , y):

    return func(func(x,y), func(x,y))
s
a = 'python'
b = 'awesome' 
print(twice(add, a,b))


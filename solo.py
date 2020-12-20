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


#What is the output of this code?
# def shout(word):
#    return word * "!"

# speak = shout
# output = speak(2)
# print(output)
# output = speak('USMAN')
# print(output)


# def add(x , y):
#     return x + y

# def twice(func , x , y):

#     return func(func(x,y), func(x,y))

# a = 'python'
# b = 'awesome' 
# print(twice(add, a,b))


# try:
#     variable = 10
#     print(variable + 'hello')
#     print(10/2)
# except ZeroDivisionError:
#     print('Zero devided by zero')
# except( ValueError , TypeError ):
#     print('Invalid type')
# finally:
#     print('this will work')

'''
after an error is raise no other block of code will
work
'''

# print(1)
# raise ValueError
# print(3)

# try:
#     num = 5 / 0
# except:
#     print('An error occure with this erro')
#     raise
'''
An assertion is a sanity-check that you can turn on or 
turn off when you have finished testing the program.
assertion only work if within code False occure
'''

# assert 2 / 2 == 4
# print('Things goes wrong')

# temp = -10
# assert (temp >= 0) , 'smaller than absolute zero'

# print('Name is invalid')


'''
Write a code that return error if user enter 
positive number
'''

# def test(name):
#     assert (name > 0) , 'Kindly enter posotive number'
#     return name
# name = int(input('Enter value'))
# test(name)

'''
file handling in python
'''

# myfile = open("word.txt", "r+")

# for i in myfile:
#     print(i)

# myfile.close()

'''
read whole content of file
'''
# myfile = open("word.txt", "r+")

# content = myfile.read(20)
# print(content)
# myfile.close()

'''
read only line by line in file
'''
# myfile = open("word.txt", "r+")

# content = myfile.readlines()
# print(content)
# myfile.close()


'''
write to the file
'''

# file = open("word.txt", "a")
# file.write("This has been written to a file")
# file.close()

# file = open("word.txt", "r")
# print(file.read())
# file.close()

'''
Working with Files

It is good practice to avoid wasting resources by 
making sure that files are always closed after 
they have been used. One way of doing this is to 
use try and finally
'''

# try:
#     f = open('word.txt')
#     print(f.read())
# finally:
#     f.close()

'''
alternate way to save data in file is use
with .... as ... operation
when with end file will autonmatically close
'''

# with open('word.txt') as name:
#     print(name.read())

'''
Dictionaries

Dictionaries are data structures used to map 
arbitrary keys to values.
Lists can be thought of as dictionaries with 
integer keys within a certain range.
Dictionaries can be indexed in the same way 
as lists, using square brackets containing 
keys.
Only immutable objects can be used as keys 
to dictionaries. Immutable objects are those 
that can't be changed. So far, the only 
mutable objects you've come across are lists 
and dictionaries. Trying to use a mutable 
object as a dictionary key causes a TypeError.
'''

# ages = {'Name':'Usman' , 'F.Name': 'IlamDin' }

# print(ages['Name'])

# primary = {
#     "red": [255, 0, 0], 
#     "green": [0, 255, 0], 
#     "blue": [0, 0, 255], 
# }
# print(primary["red"])
# print(primary["red"][2])

# squares = {1: 1, 2: 4, 3: "error", 4: 16,}
# squares[8] = 64
# squares[3] = 9
# print(squares)
# name = ['Name', 'usman', 'ilamdin']
# print(name.index('Name'))

# pairs = {1: "apple",
#         "orange": [2, 3, 4], 
#     True: False, 
#     None: "True",
# }

# print(pairs.get("orange"))
# print(pairs.get(7))  # By default return None
# print(pairs.get(12345, "not in dictionary"))

'''
Tuples


Tuples are very similar to lists, except that 
they are immutable (they cannot be changed).
Also, they are created using parentheses, 
rather than square brackets.
'''

# list1 = [1,2,3,4]
# dic   = {1:2, 2:5}
# tup   = (1,2,3,4)  # we cannot reasign the tuple value


'''
List Slices


List slices provide a more advanced way of 
retrieving values from a list. Basic list 
slicing involves indexing a list with two 
colon-separated integers. This returns a new 
list containing all the values in the old 
list between the indices.
'''
# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[1:3])
# print(squares[:7])
# print(squares[7:])
# print(squares[2::6])


'''
List Comprehensions

List comprehensions are a useful way of quickly 
creating lists whose contents obey a simple rule.
'''

# lis = [i for i in range(10)]
# print(lis)

# string formatting
# nums = [4, 5, 6]
# msg = "Numbers: {} {} {}". format(nums[0], nums[1], nums[2])
# print(msg)

# name= 'USMAN'
# print("Name it {} {} {}".format(name, name , name))

# print('{c}{b}{d}'.format(a=10 , d= 13 , b = 5 , c= 4))

# print(','.join(["spam" , "eggs" , "ham"]))
# #prints "spam, eggs, ham"

# print("Hello ME".replace("ME", "world"))
# #prints "Hello world"

# print("This is a sentence.".startswith("This"))
# # prints "True"

# print("This is a sentence.".endswith("sentence."))
# # prints "True"

# print("This is a sentence.".upper())
# # prints "THIS IS A SENTENCE."

# print("AN ALL CAPS SENTENCE".lower())
# #prints "an all caps sentence"

# print("spam ,eggs, ham".split(",")) # , shows it split here.
# #prints "['spam', 'eggs', 'ham']"


'''
Useful functions in list
'''
# lis = [1,2,3,4,5,10,2,3]


# all(lis)
# if all(num  <= 10  for num in lis):
#     print("All larger than 5")

# if any([i % 2 == 0 for i in lis]):
#     print("At least one is even")

'''
The function enumerate can be used to iterate 
through the values and indices of a list 
simultaneously.
'''
# for v in enumerate(lis):
#     print(v)

# def count_text(text , char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count

# filename = input('Enter file Name')

# with open(filename) as file:
#     text = file.read()

# print(count_text(text, 'written'))


'''
Functional Programming


Functional programming is a style of programming that 
(as the name suggests) is based around functions.
A key part of functional programming is higher-order 
functions. We have seen this idea briefly in the previous 
lesson on functions as objects. Higher-order functions 
take other functions as arguments, or return them as results.
'''
# def apply_twice(func, arg):
#     return func(func(arg))

# def add_five(x):
#     return x + 5
# # add_five is passed and then mapped func which again call
# print(apply_twice(add_five, 10))
''' 
Pure and Impure function 
'''
# Pure 
# def pure_function(x, y):
#   temp = x + 2*y
#   return temp / (2*x + y)

# #Impure functon
# some_list = []

# def impure(arg):
#   some_list.append(arg)
'''
he same is possible with functions, provided that 
they are created using lambda syntax. Functions 
created this way are known as anonymous.
This approach is most commonly used when passing a 
simple function as an argument to another function. 
The syntax is shown in the next example and consists 
of the lambda keyword followed by a list of arguments, 
a colon, and the expression to evaluate and return.
'''
# def my_func(f, arg):
#   return f(arg)

# my_func(lambda x: 2*x*x, 5)
#(lambda x: 2*x*x )(10)
# name = lambda x:2*x
# print(name(10))


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


'''
map
'''
# def my_func(arg):
#   return arg + 5

# nums  = [11 , 33 , 44 , 88 , 13 ]
# var1   = list(map(my_func , nums))
# var2   = tuple(map(my_func , nums))
# print(var1)  #return list 
# print(var2)  # return tuple
'''
filter 
'''
# var3  = list(filter(lambda x: x>30,nums))  # filter the number in list abpve 30

# print(var3)

'''
Generator
Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary 
indices, but they can still be iterated through with 
for loops.
They can be created using functions and the yield 
statement.
In short, generators allow you to declare a function 
that behaves like an iterator, i.e. it can be used 
in a for loop.
'''


# def countdown():
#     i=5
#     while i > 0:
#         yield i + 10
#         i -= 1

# for i in countdown():
#     print(i)

# def is_prime(arg):
#     if arg > 1:
#        for i in range(2, arg):
#            if (arg % i) == 0:
#                continue
#        else:
#            return arg

# def get_primes(num):
#     while True:
#         if is_prime(num):        
#             yield num
#         num += 1

# num = int(input('Enter number to test wether it is prime!'))
# get_primes(num)



# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i

# print(list(numbers(11)))

# def make_word(num):
#   word = ""
#   for ch in num:
#     word +=ch
#     yield word

# name = input('Enter word\n')
# print(list(make_word(name)))



'''
Decorators

Decorators provide a way to modify functions using 
other functions.
This is ideal when you need to extend the functionality 
of functions that you don't want to modify.
'''

# def decor(func):
#     def wrap():
#         print("============")
#         func()   # print hello world!
#         print("============")
#     return wrap

# def print_text():
#     print("Hello world!")

# decorated = decor(print_text)
# decorated()


# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#     return wrap

# @decor
# def print_text():
#     print("Hello world!")

# print_text()


'''
Recursion


Recursion is a very important concept in functional programming.
The fundamental part of recursion is self-reference - functions 
calling themselves. It is used to solve problems that can be 
broken up into easier sub-problems of the same type.

A classic example of a function that is implemented recursively 
is the factorial function, which finds the product of all 
positive integers below a specified number.
For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). 
To implement this recursively, notice that
5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. 
Generally, n! = n * (n-1)!.
'''
# def factorial(x):
#     if x == 1:   # define base case of the function
#         return 1 # A case that stop the functionality of fucntion
#     else: 
#         return x * factorial(x-1)

# print(factorial(500))


# def is_even(x):
#     if x == 0:
#         print(f'Even function nummber {x}')
#         return True
#     else:
#         return is_odd(x-1)
# def is_odd(x):
#     if x==0:
#         print(f'odd function number{x}')
#         return False
#     else:
#         return is_even(x-1)

# print(is_odd(21))
# print(is_even(22))

'''
Return some of  all list value using generator
'''
# def square(num):
#     for i in num:
#         yield i*2

# nums = [2,2,3,3,4,4]
# print(list(square(nums)))
'''
fibonacci series is the sume of  two previous proceding one
numbers

'''
# def fib(x):
#   if x == 0 or x == 1:
#     return 1
#   else:     #3         2
#             #1         0
#     return fib(x-1) + fib(x-2)
# print(fib(4))

'''
Sets are data structures, similar to lists or dictionaries. 
They are created using curly braces, or the set function. 
They share some functionality with lists, such as the use 
of in to check whether they contain a particular item.
'''
'''
To create an empty set, you must use set(), as 
{} creates an empty dictionary.

'''

# num_set = {1, 2, 3, 4, 5}
# word = 'USMAN'
# word_set = set(word)  # convert into set form
# print(word_set)
# print(3 in num_set)
# print("U" not in word_set)


'''
Set functionality almost same as list and tuple
'''
# nums = {1, 2, 1, 3, 1, 4, 5, 6}
# print(nums)
# nums.add(-7)
# nums.remove(3)
# print(nums)

'''
The union operator | combines two sets to form a 
new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set 
but not in the second.
The symmetric difference operator ^ gets items in 
either set, but not both.
'''
# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}

# print(first | second)
# print(first & second)
# print(first - second)
# print(second - first)
# print(first ^ second)
'''
Basic uses of sets include membership testing and 
the elimination of duplicate entries.
'''


"""
Final DataTructure in pythhon are

Data Structures


As we have seen in the previous lessons, Python supports 
the following data structures: lists, dictionaries, 
tuples, sets.

When to use a dictionary:
- When you need a logical association between a 
key:value pair.
- When you need fast lookup for your data, based 
on a custom key.
- When your data is being constantly modified. 
Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does
not need random access. Try to choose lists when you need a 
simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.

"""


# tup= (1,2,3,1)
# print(tup)

'''
itertools
A sander library in python

'''
# import time
# from itertools import count

# for i in count():  # we can also add parameter where count will start
#     print(i)
#     time.sleep(0.2)
#     if i >=11:
#         break
'''
other functionality of itertools
There are many functions in itertools that operate on 
iterables, in a similar way to map and filter.
Some examples:
takewhile - takes items from an iterable while a 
predicate function remains true;
chain - combines several iterables into one long one;
accumulate - returns a running total of values in 
an iterable.
'''
# from itertools import accumulate, takewhile
# nums = list(accumulate(range(8)))
# print(nums)
# print(list(takewhile(lambda x: x<= 6, nums)))
'''
Permutation & product

There are also several combinatoric functions in itertool, 
such as product and permutation.
These are used when you want to accomplish a task with all 
possible combinations of some items.
'''


# from itertools import product, permutations
# nums = [1 , 3 ,4, 5]
# letters = ("A", "B")
# print(list(product(letters, range(2))))
# print(list(permutations(letters)))
# print(list(permutations(nums))) 
#print(list(permutations(nums,3))) # give permutations of length 3 

# for i in list(permutations(nums)):
#     print(i)

'''
Combinations
'''

# from itertools import combinations , combinations_with_replacement

# # A Python program to print all 
# # combinations of given length 
# from itertools import combinations 

# # Get all combinations of [1, 2, 3] 
# # and length 2 
# comb = combinations([1, 2, 3], 2) 
# # Print the obtained combinations 
# for i in list(comb): 
# 	print (i) 






'''


Object-Oriented Programming (OOP) Vocabulary

'''


'''
Object has characteristic and do some action
these characteristic  are attributes and actions
are methods in OOP

'''

'''

class - a blueprint consisting of methods and attributes
object - an instance of a class. It can help to think of 
objects as something in the real world like a yellow pencil, 
a small dog, a blue shirt, etc. However, as you'll see later 
in the lesson, objects can be more abstract.

attribute - a descriptor or characteristic. Examples 
would be color, length, size, etc. These attributes can 
take on specific values like blue, 3 inches, large, etc.
method - an action that a class or object could take
OOP - a commonly used abbreviation for object-oriented programming
encapsulation - one of the fundamental ideas behind object-oriented 
programming is called encapsulation: you can combine functions and 
data all into a single entity. In object-oriented programming, this 
single entity is called a class. Encapsulation allows you to hide 
implementation details much like how the scikit-learn package hides 
the implementation of machine learning algorithms.

'''








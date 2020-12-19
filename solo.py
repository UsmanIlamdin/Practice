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
'''

# ages = {'Name':'Usman' , 'F.Name': 'IlamDin' }

# print(ages['Name'])
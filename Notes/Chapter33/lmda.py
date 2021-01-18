def fo(name):
    print(name)


greeting = lambda x= 'Hello World!': fo(x)

print(greeting) # this will shows memory address of function
print(greeting()) # this will print result

f = lambda x: x*2

print(f)
print(f(2))
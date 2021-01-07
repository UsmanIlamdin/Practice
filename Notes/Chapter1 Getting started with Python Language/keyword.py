# print all the ocuppied keywords list
import keyword
print(keyword.kwlist)


# Just a random check for underscore
a, b, _ = 1, 2, 3
print(_)

print(a and b)
print(a or b)
print( not a)


# complex numbers in python
print(10 + 12j)

# test tuple immutable data type
a = (1, 2, 3) 
b = ('a', 1, 'python', (1, 2))
print(b[3][1])


# hasable non double elements
h = {1,2,3,1,1}
print(h)
print(1 not in h)

#checking data type and apply certain condition

a = 10.0

if isinstance(a ,  float):
    print(f'Please enter integer! Given number is float{a}')
else:
    print('Do nothing')

# all the list operations

a = [11, 1, 1, 2, 3, 4] 
print(a.append(66))
print(a.count(1))
a.sort()
print(a)
a.pop()
a.reverse()
print(a)
# did same reverse the list as reverse method do
print(a[:-1])
print(a.index(11))


# dictionary

state_capitals = { 
    'Arkansas': 'Little Rock', 
    'Colorado': 'Denver', 
    'California': 'Sacramento', 
    'Georgia': 'Atlanta'
}

print(state_capitals.keys())
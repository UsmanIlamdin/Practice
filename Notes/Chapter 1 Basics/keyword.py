import math
from collections import defaultdict


def keyword_accupied():
    # print all the ocuppied keywords list
    import keyword
    print(keyword.kwlist)


def boleon_test():
    # Just a random check for underscore
    a, b, _ = 1, 2, 3
    print(_)
    print(a and b)
    print(a or b)
    print(not a)


def complex_number():
    # complex numbers in python
    print(10 + 12j)


def test_tuple():
    # test tuple immutable data type
    a = (1, 2, 3)
    b = ('a', 1, 'python', (1, 2))
    print(b[3][1])


def set_test():
    # hasable non double elements
    h = {1, 2, 3, 1, 1}
    print(h)
    print(1 not in h)


def type_casting():
    # checking data type and apply certain condition
    a = 10.0
    if isinstance(a,  float):
        print(f'Please enter integer! Given number is float{a}')
    else:
        print('Do nothing')


def list_operations():
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


def dic():
    # dictionary
    state_capitals = {
        'Arkansas': 'Little Rock',
        'Colorado': 'Denver',
        'California': 'Sacramento',
        'Georgia': 'Atlanta'
    }

    print(state_capitals.keys())


def default_function():
    '''
    By default add the value to eacth and every keys in dic
    '''

    state_capitals = defaultdict(lambda: 'New Joursey')
    state_capitals['a'] = 'x'
    state_capitals['b'] = 'y'
    print(state_capitals['a'])
    print(state_capitals['b'])
    print(state_capitals['usman'])


print(math.__doc__)

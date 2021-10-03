value = [2,3,6,4,4,5,5,6,3]
result = 0
for i,num in enumerate(value):
    result ^=num
print(result) 


## Explanation
"""
XOR of all the number give the smallest number
"""
"""
    1100
    1100
    0101
    1110
    0001
XOR=1010

"""
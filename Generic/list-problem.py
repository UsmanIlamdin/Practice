'''
 given two list or tuble find the
 pair of number that make 23

 e.g
 1 . [-1, 3, 2, 8 , 9 , 5]
 2 . [4 , 1, 2,10, 5, 20] 

 target is :24
'''


'''
Simple solution using the O(n^2) time complexity
Iterate through each array and find the results
'''

list1 =  [-1, 3, 2, 8 , 9 , 5]
list2 =  [4 , 1, 2,10, 5, 20 ]
for i,num1 in enumerate(list1):
    for j, num2 in enumerate(list2):
        if num1  + num2 >=24:
            print(f'the two numbers are {list1[i]} and {list2[j]}')
        else:
            continue


'''
Now try to obtimize the soluton let using
O(n) iterate only once in the list 
'''
print(list1)


import heapq

array1 = [1,2,3,4,5,5,6,1,0,44,22,21]
array2 = ['g','b','c','d','a']
array3 = ['ali', 'zara','hammad','junaid']
'''
Both nlargest and nsmallest functions take an 
optional argument (key parameter) for complicated 
data structures. 
The following example shows the use of age 
property to retrieve the oldest and the youngest 
people from people dictionary.
'''
print(heapq.nlargest(4, array1))
print(heapq.nsmallest(2 , array2)) # for alphabest compare asci
'''
find smallest items inside the iterable
is heapify and at zero th index will be samllest
'''
import heapq 
numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]
heapq.heapify(numbers) 
print(numbers)
# Output: [2, 4, 10, 100, 8, 50, 32, 200, 150, 20]
heapq.heappop(numbers) # 2 
print(numbers)
# Output: [4, 8, 10, 100, 20, 50, 32, 200, 150]
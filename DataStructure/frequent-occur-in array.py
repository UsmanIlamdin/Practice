ls1 = [2,2,2,2, 3,3,4,5,6,7,233,23]
ls1.sort()

## O(n) slution
max_count=0
max_item = None
result={}
for item in ls1:
    if item not in result:
        result[item]=1
    else:
        result[item] +=1
    if result[item]>max_count:
        max_count = result[item]
        max_item =item
print(result)
print(max_item)
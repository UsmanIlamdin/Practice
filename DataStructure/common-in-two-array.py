ls1 = [2,2, 3,3,4,5,6,7,233,23]
ls2 = [2,3,4,5,1,2,2,2,12,]

ls3=[]
for i in ls1:
    if i in ls2:
        ls3.append(i)
    else:
        continue
print(ls3)
print(list(set(ls3)))




"""
##sorted array solution
ls1.sort()
ls2.sort()
result = []
i=0
j=0
while i< len(ls1) and j < len(ls2):
    if ls1[i]==ls2[j]:
        result.append(ls1[i])
        i+=1
        j+=1
    elif ls1[i]>ls2[j]:
        j+=1
    else:
        i+=1
print(result)

"""





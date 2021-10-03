string = "aabcddc"
count=0
dic = {}
for i in string:
    if i  not in dic:
        dic[i] = 1
    else:
        dic[i] +=1
for key in dic:
    if dic[key]==1:
        print(key)
    
print(dic)
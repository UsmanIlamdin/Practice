

value = [2,3,4,5,6,7,8,3]

for i, num0 in enumerate(value):
    for j, num1 in enumerate(value):
        count =0
        if i==j:
            continue
        elif num0==num1:
            print(i,num0)
            print(j,num1)
            break
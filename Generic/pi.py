
'''
using two random number find the value of 
pi using given data.
'''

# importing the required module 
import matplotlib.pyplot as plt 
import random





def find_pi(points):
    circle_points = 0
    total_points = 0
    X_list = []
    Y_list = []
    for _ in range(points):
        x = random.uniform(0 , 1)
        y = random.uniform(0 , 1)
        X_list = X_list.append(list(x))
        Y_list = Y_list.append(list(y))
        distance = x**2 + y**2
        if distance <= 1:
            circle_points +=1
        total_points +=1
    #plotting points as a scatter plot 
    plt.scatter(X_list, Y_list, label= "stars", color= "green",  
                marker= ".", s=20) 
    #x-axis label 
    plt.xlabel('x - axis') 
    #frequency label 
    plt.ylabel('y - axis') 
    #plot title 
    plt.title('My scatter plot!') 
    # showing legend 
    plt.legend()   
    # function to show the plot 
    plt.show() 
    return 4* circle_points/total_points

y = []
for i in range(10):
    x = random.uniform(0,2)
    y = y.join(list(x))
    print(y)

# print(find_pi(100))


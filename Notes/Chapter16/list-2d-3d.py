# lst_2d=[[1,2,3],[4,5,6],[7,8,9]]


# lst_3d=[[[111,112,113],[121,122,123],[131,132,133]],
#         [[211,212,213],[221,222,223],[231,232,233]], 
#         [[311,312,313],[321,322,323],[331,332,333]]]

# # retrive 2d list
# print(lst_2d[0])
# print(lst_2d[1][2])

# #retrive 3d list

# print(lst_3d[0])
# print(lst_3d[1][2])
# print(lst_3d[1][2][2])

sum_A = 0.0
nums = [3,74.5, 49,17.5,56.5,37.5,50.5,52.5,69.5,51.5,56.5,40,58.5,67.5,
        41,58.5,45,29.5,41.5,34.5,32,33.5,34,26.5,64,25,51.5,56.5,26,20.5,
        2,63.5,45,41,47,60.5,49.5,59.5,33.5,50,33.5,45,57,43.5,23.5,26,45.5]
for index, num in enumerate(nums):
        # print(index)
        # print(num)
        sum_A = sum_A+num
        # print("\n")
print(sum_A/len(nums))




sum_B = 0.0
nums = [29,20,42,42.5,65.6,42,60,58.5,41.5,34.5,42,40.5,28.5,24,54,29,32.5,
        42,3,38.5,36,19.5,41,47.5,30.5,23,6,30,30,50,0,45,42,52,21,53.5,26.5,
        35,53.5,52,45,42.5,55.5,48.5,26.5,21]
for index, num in enumerate(nums):
        # print(index)
        # print(num)
        sum_B = sum_B+num
        # print("\n")
print(sum_B/len(nums))



total_sec = [3,74.5, 49,17.5,56.5,37.5,50.5,52.5,69.5,51.5,56.5,40,58.5,67.5,
        41,58.5,45,29.5,41.5,34.5,32,33.5,34,26.5,64,25,51.5,56.5,26,20.5,
        2,63.5,45,41,47,60.5,49.5,59.5,33.5,50,33.5,45,57,43.5,23.5,26,45.5,
        29,20,42,42.5,65.6,42,60,58.5,41.5,34.5,42,40.5,28.5,24,54,29,32.5,
        42,3,38.5,36,19.5,41,47.5,30.5,23,6,30,30,50,0,45,42,52,21,53.5,26.5,
        35,53.5,52,45,42.5,55.5,48.5,26.5,21]
for index, num in enumerate(total_sec):
        # print(index)
        # print(num)
        sum_total = sum_B+num
        # print("\n")
print(sum_total/len(nums))
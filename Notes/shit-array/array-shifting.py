def shift_list(array , s):


    s %=len(array)
    print(s)
    s *= -1
    print(s)
    # shift array with list slicing 
    shifted_array = array[s:] + array[:s]
    print(s)
    return shifted_array
my_array = [1, 2, 3, 4, 5]

print(shift_list(my_array, -7))
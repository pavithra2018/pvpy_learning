#
#===================================================================================
#
#NAME                 : largest_elements_in_array.py
#DATE                 : 24th oct, 2019
#DESCRIPTION          : A python program to find the largest element in the array.
#AUTHOR               : K pavithra
#
#====================================================================================
#
"""
    This program is to find the largest element in the array
    
    PSEUDOCODE:
        1. prompt the user for the input
        2. take a variable maximunm and initialize it to first element of the array i.e;array[0]
        3. itterate a loop through the array and check if the array value is greater than maximum value
        4. if yes move the array value to the maximum variable
        5. continue this till the end odf the array
        6. finally print the maximum value.
        
"""

array = []
number = int(input("enter the no.of numbers:"))
for i in range(0 , number) :
    print("enter a number:")
    temp = int(input())
    #for adding the element to the array.
    array.append(temp)
print(array)
maximum = array[0]
for x in range(0 , len(array)) :
    if array[x] > maximum :
        maximum = array[x]
print("largest element present in the array is:", maximum)        
        
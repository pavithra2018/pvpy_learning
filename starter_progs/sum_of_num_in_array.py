#
#======================================================================
#
#NAME                 : sum_of_num_in_array.py
#DATE                 : 24th oct, 2019
#DESCRIPTION          : A python program to add the numbers in the array.
#AUTHOR               : K pavithra
#
#======================================================================
#
"""
    This program is to calculate the sum of the numbers in the array.
    
    PSEUDOCODE :
        1. create an empty array
        2. read the input from the user dynamically
        3. add the elements of the array
        4. print the sum
"""

# Statically reading elements into array.
#array = [1,20,40,50]

#Dynamically reading elements into the array.
array = []
number = int(input("enter the nuber of elements to be summed:"))
for i in range(0 , number) :
    print("enter a number:")
    temp = int(input())
    #for adding the element to the array.
    array.append(temp)
print(array)
print(dir(array))
#Logic to add the elements of the array.
sum = 0
for x in array :
    sum = sum + x 
print("sum of numbers in the array are:", sum)
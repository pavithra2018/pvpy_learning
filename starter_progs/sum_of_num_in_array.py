#
#======================================================================
#
#NAME                 : sum_of_num_in_num_array.py
#DATE                 : 24th oct, 2019
#DESCRIPTION          : A python program to add the numbers in the num_array.
#AUTHOR               : K pavithra
#
#======================================================================
#
"""
    This program is to calculate the sum of the numbers in the num_array.
    
    PSEUDOCODE :
        1. create an empty num_array
        2. read the input from the user dynamically
        3. add the elements of the num_array
        4. print the sum
"""

# Statically reading elements into num_array.
#num_array = [1,20,40,50]

#Dynamically reading elements into the num_array.
num_array = []
number = int(input("Enter the nuber of elements to be summed: "))
for ncount in range(0 , number) :
    print("Enter a number: ", end='')
    temp = int(input())
    #for adding the element to the num_array.
    num_array.append(temp)
print(num_array)
print(dir(num_array))
#Logic to add the elements of the num_array.
nums_sum = 0
for lnum in num_array :
    nums_sum = nums_sum + lnum
print("Sum of numbers in the num_array are:", nums_sum)

# We can use sum() built-in method also
print("Sum of numbers in the list {} is :{}".format( num_array, sum(num_array)))



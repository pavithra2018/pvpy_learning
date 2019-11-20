"""
#
#========================================================================================
#
#NAME                 : simple_intreest.py
#DATE                 : 24th oct, 2019
#DESCRIPTION          : Python program to interchange first and last elements in a list
#AUTHOR               : K pavithra
#
#========================================================================================
#
"""
# declare a empty array
array = []
# ask for the user to enter the range of numbers to be entered
number = int(input("number of numbers to be entered:"))
# read the values from the user
for i in range(0, number):
    print("enter a number:")
    a = int(input())
    array.append(a)
# print the values inside the array
print("elements inside array are:", array)
# initially store the first element of the array in a variable temp
temp = array[0]
# copy the lat element to zeroth index of the array
array[0] = array[len(array)-1]
# copy the value inside temp to last index of the array
array[len(array)-1] = temp
# finally print the array which contain the interchanged values
print("elements after interchange are:", array)

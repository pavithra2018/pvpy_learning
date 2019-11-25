#
#======================================================================
#
#NAME                 : duplicates_array.py
#DATE                 : 25th nov, 2019
#DESCRIPTION          : Python Program to print duplicates from a list of integers
#AUTHOR               : K pavithra
#
#======================================================================
#
'''
    Pseudocode :
        1. declare a list as list1 and assign values to it
        2. declare an empty list as list2
        3. sort the elements of the list by sort()
        4. declare a variable count and assign it to zero
        5. until count value less than or equal to length of list1
        6. compare the elements and if they are equal copy it to list2 and print
        7. else move to next element and repeat the loop until count is greater than length(list1)
'''
list1 = [ 30, 10, 10, 70, 90, 30, 20, 10, 70 ]
list2 = []
'''
number = int(input("number of numbers to be entered:"))
for i in range(0, number):
    print("enter a number:")
    list1 = int(input())
    array_1.append(list1)
'''
#print(dir(list1))
'''
array_1.sort()
print(array_1)
array_2 = []
for i in range(0, len(array_1)-1) :
    if(array_1[i] == array_1[i + 1]) :
        print(array_1[i])
        array_2.append(array_1[i])
'''
print(list1)
print("duplicate elements:")
list1.sort()
print(list1)
count = 0
while count < (len(list1) - 1) :
    if list1[count] == list1[count + 1] :
        while list1[count] == list1[count + 1] :
            count = count + 1
        list2 = list1[count]
        print(list2)
    else :
        count = count + 1

        

        

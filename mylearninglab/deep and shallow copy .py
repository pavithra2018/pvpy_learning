#Program to demostrate deepcopy

import copy
print(dir(copy))
# declaring a list and printing the list

list1 = [1,2,3,4]
print("list1 contains:",list1)
# copying the items in list1 to list2 by using deepcopy() and printing them
list2 = copy.deepcopy(list1)
print("list2 contains:", list2)
# adding an element to list2 and printing them to see the changes happened in list2
list2[2] = 10
print("after adding element list2 contains:",list2)
# checking the original list i.e; list1 after making changes to list2.
print("the original list1 after adding the element is", list1)
print("=" * 100)

#program to demostrate shallowcopy
list3 = copy.copy(list1)
print("list3 contains:", list3)
print("the original list1 before adding the element is",list1)
list3[3] = 20
print("after adding element list3 contains:",list3)
print("after adding element list1 contains:",list1)

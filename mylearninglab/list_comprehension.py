"""
    List comprehension allows us to create list with less code.
    List comprehension uses [] in its syntax.
    It returns a list of values.
"""

# creating a list
num_list = [10,20,25,30,10,35,45,10,50,25,20]
# removing duplicates from the list using set()
new_list = set(num_list)
# sorting the list in ascending order using sort()
new_list.sort()
print(new_list)
print(num_list)
print("the even is in the list are:")
print([number for number in num_list if (number % 2) == 0])
print("the odd is in the list are:")
print([number for number in num_list if (number % 2) != 0])
print("the list after removing duplicate elements:")
print(set([number for number in num_list if (num_list.count(number)) > 1]))
print("the unique elements in the list are:")
print(set([number for number in num_list if (num_list.count(number) == 1)]))
print(sum(num_list))

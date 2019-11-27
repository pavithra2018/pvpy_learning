"""
    The symmetric difference of two sets A and B is the set of elements which are in 
    either of the sets A or B but not in both.
    
    syntax :
    A.symmetric_difference(B)
        or
    A ^ B
"""


mobile_number = {9,9,8,5,4,7,2,3,7,6}
all_numbers = {0,1,2,3,4,5,6,7,8,9}
# ^ symbol is symmetric difference.
missing_numbers = mobile_number ^ all_numbers

print(sorted(missing_numbers))


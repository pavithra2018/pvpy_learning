"""
#
#=================================================================================
#
#NAME                 : armstrong.py
#DATE                 : 20th nov, 2019
#DESCRIPTION          : python program to Print Armstrong numbers within given range.
#AUTHOR               : K pavithra
#
#=================================================================================
#
"""
# prompt the user to specify the lowerlimit
lower_limit = int(input("enter the lower limit:"))
# prompt the user to specify the upperlimit
upper_limit = int(input("enter upper limit:"))
# itterate the loop until till the given range
for number in range(lower_limit,upper_limit+1) :
    # initialize sum
    my_sum = 0
    # store the length of the number into variable length
    length = len(str(number))  
    #copy the value in number into variable temp
    temp = number
    # itterate the loop
    while temp > 0:
        #calculate sum of power of numbers
        digit = temp % 10
        my_sum = (my_sum + (digit ** length))
        temp = temp // 10
    # check if the number and sum are equal and print the numbers
    if number == my_sum :
        print("armstrong numbers are:", number)
 
        
        

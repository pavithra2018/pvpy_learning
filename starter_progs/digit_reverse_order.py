#
#===========================================================================================
#
#NAME                 : digit_reverse_order.py
#DATE                 : 26th oct, 2019
#DESCRIPTION          : A python program to find the reverse order of given number.
#AUTHOR               : K pavithra
#
#===========================================================================================
#
"""
    This program is to extract and print the digits of a number in reverse order.
    Inorder to do this we have used the division(//) and modulo division(%) opertors.
    // : the output of this is the quotient
    %  : the output of this is the reminder
    
    PSEUDOCODE :
        1. read the input from the user
        2. initialize reverse variable to zero
        3. now multiply the reverse variable with 10 and add to the reminder by performing(number % 10)
        4. collect the quotient from (number // 10) and store in number
        5. continue this process till the number is greater than zero
        6. finally print the reversed number
"""
number = int(input("enter the number to be reversed: "))
reverse = 0
print("{} is the entered number".format(number))
while (number > 0) :
    reverse = ((reverse * 10) + (number % 10))
    number = number // 10
print("{} is the reversed number".format(reverse))
    
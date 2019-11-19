#
#======================================================================
#
#NAME                 : compound_intreest.py
#DATE                 : 24th oct, 2019
#DESCRIPTION          : A python program to find compound intrest.
#AUTHOR               : K pavithra
#
#======================================================================
#

"""
    This program is to calculate the compound intrest.
    
    FORMULA :
        Compound Interest = P(1 + R/100)t
    Where,
    P is principle amount
    R is the rate of intrest and
    t is the time span

"""
#import math
principal_amount = float(input("enter the principal amount value: Rs."))
rate_of_intrest = float(input("enter the rate of intrest: Rs."))
time = float(input("enter the time in years:"))
compound_intrest = pow((1 + (rate_of_intrest/100)),time)*principal_amount
#compound_intrest =((1 + (rate_of_intrest/100))**time) * principal_amount
print("compound intrest is:", compound_intrest)




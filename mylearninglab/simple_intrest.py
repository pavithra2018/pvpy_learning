#
#======================================================================
#
#NAME                 : simple_intreest.py
#DATE                 : 24th oct, 2019
#DESCRIPTION          : A python program to find simple intrest.
#AUTHOR               : K pavithra
#
#======================================================================
#
"""
    This program is to calculate the simple intrest.
    
    FORMULA :
        Simple intrest = (P * T * R)/100
        Where,
        P is the principle amount
        T is the time and
        R is the rate of intrest

"""

principal_amount = float(input("enter the principal amount value: Rs."))
rate_of_intrest = float(input("enter the rate of intrest: Rs."))
time = float(input("enter the time in years:"))
simple_intrest = ((principal_amount * rate_of_intrest * time)/100)
print("simple_intrest : ", simple_intrest)
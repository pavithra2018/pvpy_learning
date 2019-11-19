"""
    A program to find the even numbers between the given range using range()
    
    syntax of range() :
        range(start,stop,step)
        where, stop value is exclusive. 
"""

num1 = int(input("enter the first value"))
num2 = int(input("enter the second value"))
for number in range(num1 , num2 , 1) :
    if number % 2==0 :
        print(number, end=" ")
    
    

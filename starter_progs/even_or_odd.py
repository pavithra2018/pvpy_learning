#num = int(input("enter the value:"))
#if num%2==0 :
    #print(num, "is even")
#else :
    #print(num, "is odd")

    
import sys
#print('Please enter a number: ')
#number = int(input())
#input for command line arguments from cmd prompt.
number = int(sys.argv[1])
print("enter a positive integer") if number < 0 else print("you have given a positive integer")
if ((number % 2) == 0):
    print(number, "is even")
else:
    print(number, "is odd")

    
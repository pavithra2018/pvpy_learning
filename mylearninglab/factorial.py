#import sys
#n = int(sys.argv[1])
n = int(input("enter the value:"))
fact = 1
while n > 1 :
    fact = fact * n
    n = n - 1
print("factorial of given number is:")
print(fact)

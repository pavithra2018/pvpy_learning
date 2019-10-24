#import sys
#n = int(sys.argv[1])
n = int(input("enter the value:"))
i = n
fact = 1
while i>=1 :
    fact = fact*i
    i = i-1
print("factorial of given number is:")
print(fact)

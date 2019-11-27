#n = int(input("enter a value "))
import sys
n = int(sys.argv[1])
i = 3
n1 = 0
n2 = 1
print("fibonacci series upto given range:")
print(n1, end = '\n')
print(n2)
while  i<=n :
    n3 = n1 + n2
    print(n3)
    n1 = n2;
    n2 = n3;
    i = i+1;

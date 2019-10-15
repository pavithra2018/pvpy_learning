n = int(input("enter a value"))
a = n
rev = 0
while(n>0) :
    rev = rev*10+n%10
    n=n//10
if(a==rev) :
    print(a, "is a palindrome")
else :
    print(a, "is not a palindrome")
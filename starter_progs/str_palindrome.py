string = input("enter a string")
rev_string = string[::-1]
print("reversed string is:",rev_string)
if string==rev_string :
    print(string, "is a palindrome")
else :
    print(string, "is not a palindrome")
"""
Rules to be checked   :
===================
1. At least 1 letter between [a-z] and 1 letter between [A-Z]
2. At least 1 number between [0-9]
3. At least 1 character from [$#@]
4. Minimum length 6 characters and Maximum length 16 characters
5. Should not have any spaces in between

"""
import re
x = True
while x:
    p = input("Input new password: ")
    if (len(p)<6 or len(p)>16):
        print("Not a valid password")

    elif not re.search("[a-z]",p):
        print("Not a valid password")

    elif not re.search("[0-9]",p):
        print("Not a valid password")

    elif not re.search("[A-Z]",p):
        print("Not a valid password")

    elif not re.search("[$#@]",p):
        print("Not a valid password")

    elif re.search("\s",p):
        print("Not a valid password")

    else:
        print("Congrats!, New password is set")
        x=False
        break


    

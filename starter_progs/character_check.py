#Find if give character is alphabet, Digit or special character?
print("enter any character:")
character = input()
if((character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z')): 
    print("The Given character",character, "is an Alphabet") 
elif(character >= '0' and character <= '9'):
    print("The Given character",character, "is a Digit")
else:
    print("The Given character",character, "is a Special character")
#Check if given alphabet is in lower/upper case
print("enter any alphabet:")
alphabet = input()
if((alphabet >= 'a' and alphabet <= 'z')) :
    print("the given alphabet", alphabet, "is in lowercase")
elif((alphabet >= 'A' and alphabet <= 'Z')) :
    print("the given alphabet", alphabet, "is in uppercase")
else :
    print("only alphabets are allowed")

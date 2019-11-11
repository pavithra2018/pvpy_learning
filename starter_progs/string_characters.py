#
#===========================================================================================
#
#NAME                 : string_characters.py
#DATE                 : 25th oct, 2019
#DESCRIPTION          : A python program to find the character count in a given text.
#AUTHOR               : K pavithra
#
#===========================================================================================
#
"""
    This program is to find the character count in agiven text.
    If any charcter in the text is not equal to space then count 
    value is incremented.
    If character is equal to space the loop again itterates 
    amd finally count value is printed.
    
    PSEUDOCODE :
        1. first read the text from the user
        2. initialize count to zero
        3. now itterate a variable through the text
        4. check if character is equal to space
        5. if yes continue the itteration
        6. if no increment count value
        7. repeat this till the text ends and print the count value
"""

string = input("enter the text:")
count = 0
for x in string :
    if (x != " ") :
        count = count + 1
print("number of characters in %s is %d" %(string, count))

    
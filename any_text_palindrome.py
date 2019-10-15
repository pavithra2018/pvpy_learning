#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python -f
#==================================================================================================
#
# NAME        : any_text_palindrome.py
# DATE        : 15th Oct, 2019
# DESCRIPTION : A Python program to find if a given text is a Palindrome or not
# AUTHOR      : Bhaskar Varadaraju
# VERSION     : 1.0
#
# Change History:
#   VBhaskar    15th Oct, 2019      Created     Added initial version of file
#   VBhaskar    15th Oct, 2019      Edited      Changed logic to use slicing which is faster.
#
#==================================================================================================
"""
    This program is to check if the given text is Palindrome or NOT.
    We reverse the text and compare with original text for equality.
    The text is a Palindrome is they are equal, else the text is NOT a palindrome.

    Pseudocode:
        1. Prompt the user for text
        2. Read the text from user
        3. Reverse the user given text
        4. Compare original text with reversed text for equality
        5. IF check is true then it is a palindrome
           ELSE it is not a palindrome
"""

# Prompt and read text from user
text_data = input("Enter a value: ")
# Rereser the given text using slicing and then compare if they are equal
if text_data[::-1] == text_data:
    print(n, "is a Palindrome")
else:
    print(n, "is NOT a Palindrome")




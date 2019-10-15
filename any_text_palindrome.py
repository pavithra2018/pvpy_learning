#
#===================================================================================
#
# NAME        : any_text_palindrome.py
# DATE        : 15th Oct, 2019
# DESCRIPTION : A Python program to find, if a given text is a Palindrome or not.
# AUTHOR      : V Bhaskar
# VERSION     : 1.0
#
# Change History:
#   VBhaskar    15/10/2019  Created     Added initial version of file
#   VBhaskar    15/10/2019  Edited      Changed logic to use slicing which is faster.
#
#=====================================================================================
#
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

# Check if the text is given from Command line interface
import sys
if len(sys.argv) == 2:
    print('Number of cli arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    text_data = str(sys.argv[1])
else:
    # Check if the text is given from environment variable
    import os
    try:
        text_data = os.environ['TEXT_DATA']
        print('TEXT_DATA is set in the environment.')
    except KeyError: 
        # Prompt user and read text from console
        text_data = input('Please enter a text: ')
    finally:
        # we have the final text_data to validate
        print(text_data, 'is the text given.')

# Reverse the given text using slicing and compare with original text
if text_data[::-1] == text_data:
    print(text_data, "is a \033[01m\033[34mPalindrome \033[00m")
else:
    print(text_data, "is \033[01m\033[34mNOT a Palindrome \033[00m")


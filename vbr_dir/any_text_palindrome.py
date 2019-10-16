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
import os
import sys

LOG_FILENAME = '/tmp/' + str((sys.argv[0]).rsplit('.',1)[0]) + '.log'
# This is a method to print given message
# Arguments: 
#       msg - The message to be printed
def my_print(msg):
    print(msg)

## Ensure that only 'bhasvara' user can run this program.
if os.environ['USER'] != 'bhasvara':
    my_print("ERROR: This program must be run by 'bhasvara' user only.")
    exit(1)

# Check if the text is given from Command line interface
if len(sys.argv) >= 2:
    #my_print('Number of cli arguments: ' + str(len(sys.argv)) + ' arguments.')
    #my_print('Argument List: ' + str(sys.argv))
    my_print('The last argument from CLI was: ' + str(sys.argv[-1]))
    my_print('Word of text was given via CLI arguments')
    #my_print(LOG_FILENAME)
    text_data = str(sys.argv[1])
else:
    # Check if the text is given from environment variable
    try:
        text_data = os.environ['TEXT_DATA']
        my_print('Word of text was given via TEXT_DATA variable in the environment.')
    except KeyError: 
        # Prompt user and read text from console
        # Ternary operator => text_data = input('Please enter a text: ') if sys.stdin.isatty() else input()
        if sys.stdin.isatty():
            text_data = input('Please enter a word of text: ')
        else:
            # If we are not having a stdin() attached then read directly without prompy. 
            #   Ex: PIPE (|) input from echo
            text_data = input()
    finally:
        # we have the final text_data to validate
        my_print('\"' + text_data + '" is the given word of text.')

# Reverse the given text using slicing and compare with original text
if text_data[::-1] == text_data:
    my_print(text_data + ' is a Palindrome')
else:
    my_print(text_data + ' is NOT a Palindrome')


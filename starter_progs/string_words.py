#
#===========================================================================================
#
#NAME                 : string_words.py
#DATE                 : 25th oct, 2019
#DESCRIPTION          : A python program to find the words count in a given text.
#AUTHOR               : K pavithra
#
#===========================================================================================
#
"""
    This program is to find the number of words in the given sentence.
    We calculate the spaces first and adding one to that gives the word count.
    
    PSEUDOCODE:
        1. read the text from user
        2. initialize space_count to zero
        3. iterate the loop through the text
        4. check if character equal to space
        5. if yes increment the space_count value 
        6. if no iterate again till the end of the text
        7. finally print the word count by incrementing the space_count by one
"""
"""
import time
string = input("enter the text:")
space_count = 0
start = time.time()
for x in string :
    #time.sleep(1)
    if (x == " ") :
        space_count = space_count + 1
end = time.time()
print("time taken by for loop is:", start-end)
number_of_words = space_count + 1
print("the number of words in the text are {}".format(number_of_words))
"""

string = "finally print the word count by incrementing the space_count by one"
print("the number of words  in the given string are:", len(string.split()))

print( len(list(map( lambda word: word.strip(), string.split()))))


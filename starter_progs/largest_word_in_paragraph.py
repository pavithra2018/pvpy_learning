text = "To provide schools with the tools, training and ongoing support they need to create a culture of conservation and natural resource stewardship within their community."
#print(type(text))
k = text.split()
#print(type(k))
#print(k)
length = 0
long_word = str()
for index, i in enumerate( k, 1 ):
    print ("word at {} is {}".format(index, i))
    if len(i) > length :
        long_word = i
        length = len(i)
print("the longest word in the text is:", long_word, "and its length is ", length)
print(index)
print(dir(long_word))
print(long_word.upper())
"""
 capitalize,'casefold', 'center', 'count', 'encode', 'endswith', 
 'expandtabs', 'find', 'format', 'format_map', 'index', 
 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
print(long_word.capitalize())
print(long_word.count('o'))


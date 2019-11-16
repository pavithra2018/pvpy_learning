"""
number = [1, 2, 3, 4]
color = ['red', 'green', 'blue', 'black', 'grey']
for (a, b) in zip(number, color) :
    print(a, b)
"""
"""
for number , color ,fruit in zip([1,2,3,4], ['red', 'yellow', 'green'], ['apple', 'mango', 'grape']) :
    print("{} {} {}".format(number, color, fruit))
"""
# BY USING LIST COMPREHENSION :
a = (1, 2, 3)
b = (4, 5, 6)
[print('list1:', i, '; list2:', j) for i, j in zip(a, b)]
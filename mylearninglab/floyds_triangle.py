"""
    Floyd's triangle is a right angle triangle of natural numbers i.e;
    1
    2 3
    4 5 6
    7 8 9 10
"""
number = int(input("enter the number of rows:"))
start = 1
for row in range(1, (number + 1)) :
    for dummy in range(1, (row + 1)) :
        print("%3d" %start, end=" ")
        start = start + 1
    print()


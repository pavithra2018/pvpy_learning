"""
    Floyd's triangle is a right angle triangle of natural numbers i.e;
    1
    2 3
    4 5 6
    7 8 9 10
"""
number = int(input("enter the number of rows:"))
k = 1
for i in range(1, (number + 1)) :
    for j in range(1, (i + 1)) :
        print("%3d" %k, end=" ")
        k = k + 1
    print()


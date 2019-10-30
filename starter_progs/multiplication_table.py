number = int(input("enter a number:"))
print("multiplication table of", number, "is :")
for i in range(1, 11) :
    print("{:4d} X{:4d} ={:4d}".format(number, i, (number * i)))
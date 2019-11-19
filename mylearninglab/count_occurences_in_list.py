array = []
number = int(input("number of numbers to be entered:"))
for i in range(0, number):
    print("enter a number:")
    a = int(input())
    array.append(a)
print("elements inside array are:", array)
print(dir(array))
for x in range(0, len(array)):
    a = array.count(array[x])
    print(array[x], "is repeated", a,"times" )

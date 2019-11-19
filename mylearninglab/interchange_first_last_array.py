array = []
number = int(input("number of numbers to be entered:"))
for i in range(0, number):
    print("enter a number:")
    a = int(input())
    array.append(a)
print("elements inside array are:", array)
temp = array[0]
array[0] = array[len(array)-1]
array[len(array)-1] = temp
print("elements after interchange are:", array)

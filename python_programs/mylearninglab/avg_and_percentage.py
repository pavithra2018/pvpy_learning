array = []
number = int(input("enter number of subjects:"))
for i in range(0, number):
    print("enter marks of subject",i, " :")
    a = float(input())
    array.append(a)
print("marks of", number,"subjects:", array)
total = 0
for i in range (0, number) :
    total = total + array[i]
average = (total / number)
percentage = (total / (number * 100)) * 100
print("total marks = %.2f" %total)
print("average marks = %.2f" %average)
print("percentage marks = %.2f" %percentage)
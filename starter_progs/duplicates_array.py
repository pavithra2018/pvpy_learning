a = [ 30, 10, 10, 70, 90, 30, 20, 10, 70 ]
b = []
'''
number = int(input("number of numbers to be entered:"))
for i in range(0, number):
    print("enter a number:")
    a = int(input())
    array_1.append(a)
'''
#print(dir(a))
'''
array_1.sort()
print(array_1)
array_2 = []
for i in range(0, len(array_1)-1) :
    if(array_1[i] == array_1[i + 1]) :
        print(array_1[i])
        array_2.append(array_1[i])
'''
print(a)
print("duplicate elements:")
a.sort()
print(a)
count = 0
while count < (len(a) - 1) :
    if a[count] == a[count + 1] :
        while a[count] == a[count + 1] :
            count = count + 1
        print(a[count])
    else :
        count = count + 1

        

        

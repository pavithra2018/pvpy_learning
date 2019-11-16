"""
numlist = []
number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    numlist.append(value)
numlist.sort()
print("The Smallest Element in this List is : ", numlist[0])
print("The Largest Element in this List is : ", numlist[number - 1])
"""
numlist = [10,-4,3,2,40,6,22,11,7,45]
print(dir(numlist))
print(sorted(numlist))
print("The Smallest Element in this List is : ", numlist[0])   # can also use min(numlist)
print("The Largest Element in this List is : ", numlist[len(numlist)-1])# can also use max(numlist)

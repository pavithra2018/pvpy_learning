num_list = [10,20,25,30,10,35,45,10,50,25,20]
new_list = [set(num_list)]
new_list.sort()
print(new_list)
print(num_list)
print("the even numbers in the list are:")
print([i for i in num_list if (i % 2) == 0])
print("the odd numbers in the list are:")
print([i for i in num_list if (i % 2) != 0])
print("the list after removing duplicate elements:")
print(set([i for i in num_list if (num_list.count(i)) > 1]))
print("the unique elements in the list are:")
print(set([i for i in num_list if (num_list.count(i) == 1)]))
print(sum(num_list))

import input 
print(input.number1)
if (input.number1 % 2) == 0 :
    print("{} is even".format(input.number1))
else :
    print("{} is not even".format(input.number1))
    
from input import number1
print(number1)

from input import list1 as my_num_list
print(my_num_list)
print(input.list1)

from input import list1
print(list1)
#numbers = (1,2,4,3,5,7,8,6,9)
count_odd = 0
count_even = 0
for x in range(100, 1000) :
    if (x % 2 == 0) :
        count_even = count_even + 1
    else :
        count_odd = count_odd + 1
print('*' * 50)       
print("no.of even numbers are:",count_even)
print("no.of odd numbers are:",count_odd)
print('*' * 50) 
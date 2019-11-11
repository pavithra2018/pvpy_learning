lower_limit = int(input("enter the lower limit:"))
upper_limit = int(input("enter upper_limit:"))
for num in range(lower_limit , upper_limit+1) : 
    my_sum = 0
    a = len(str(num))  
    temp = num
    while temp > 0:
        digit = temp % 10
        my_sum = (my_sum + (digit ** a))
        temp = temp // 10
    if num == my_sum :
        print("armstrong numbers are:", num)
 
        
        
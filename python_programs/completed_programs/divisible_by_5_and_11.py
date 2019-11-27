number = int(input("enter a number:"))
#if number > 0 :
if ((number % 5 == 0) and (number % 11 == 0)) :
    print("{} is divisible by 5 and 11".format(number))
else :
    print("{} is not divisible by 5 and 11".format(number))
#else :
    #print("enter a positive number")

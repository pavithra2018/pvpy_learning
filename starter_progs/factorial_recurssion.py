def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)
# n * n-1 
number = int(input("enter the number:"))
result = factorial(number)
print("The factorial of {} is {}".format(number,result))
print("The factorial of %d is %d" % (number,result))
print("The factorial of", number, "is", result)

        
        
        
    

def my_print():
    print("Hello! good morning")
def name_print(name = 'bhaskar'): # if we pass any parameter it will print that parameter
    print("Hello", name)          # if we not pass any parameter it will print the default parameter.
def odd_even(number):
    if number % 2 == 0 :
        print("{} is even number".format(number))
    else :
        print("{} is odd number".format(number))
def sum_two(num1,num2):
    total = num1 + num2
    print("sum of two numbers is:",total)
def sum_many(*numbers): 
    n_sum = 0
    for i in numbers :
        n_sum = n_sum + i 
    print(n_sum)
    return

    
my_print()
name_print('pavithra')
name_print()
odd_even(10)
sum_two(10,20)
sum_many(10,20,30,40,50)
sum_many()
sum_many(20)
sum_many('i', 'k')
x = sum_many()


        
    
    
    
    


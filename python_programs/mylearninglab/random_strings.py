""
#
#======================================================================
#
#NAME                 : simple_intreest.py
#DATE                 : 24th oct, 2019
#DESCRIPTION          : A python program to generate random string 
#AUTHOR               : K pavithra
#
#======================================================================
#
"""






"""
import random
v1 = random.randint(1,7)
print(v1)

wishes = ['hello','hi','hey','dear']
v2 = random.choice(wishes)
print(v2 +', pavi!') 

colors = ['red','blue','green']
results = random.choices(colors, k=10)
print(results) 

deck = list(range(1, 53))
h1 = random.sample(deck, k=5)
print(h1)
h2 = random.choices(deck, k=5)
print(h2)
"""
import random
number = int(input("enter a 3-digit number:"))
for i in range(100,999):
    value = random.randint(100,999)
    print(value)
    if value == number :
        print(number, "is found after", i, "iterations")
        break
    
    
    
    















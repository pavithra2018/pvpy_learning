t1 = (1,2,3)
print(type(t1)) 
print(dir(t1))
str(t1)
print(t1)

t2 = 1,2,4
print(type(t2))
print(t2)
't2'
print(t2)
t2 += (3,)
print(t2)

t3 = (1, )
t3 += (2,)
print(t3)

T = tuple('geeks') 
a, b, c, d, e = T 
#b = c = '*'
#T = (a, b, c, d, e) 
print(a)
print(T) 
print(type(T))
T = (a, b, c, d, e)
print(T)

import time
print(time.time())



















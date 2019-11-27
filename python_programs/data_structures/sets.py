a = {1,2,3,4}
b = {3,4,5,6,7}
c = a.intersection(b)#a&b
print(c)
d = a.union(b)#a|b
print(d)
e = c.issubset(a)
print(e)
f = c.issuperset(a)
print(f)
g = b.difference(a)
print(g)
h = b.symmetric_difference(a)
print(h)
i = {}
i = a.copy()
print(i)
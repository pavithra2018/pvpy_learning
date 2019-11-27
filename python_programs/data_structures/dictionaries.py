d = {1:'string value', 2:[1,2]}
print(d.keys())
print(d.values())
print(d.items())
print(d[1])
print(type(d))

d1 = {'first' : 'good', 'second' : 'morning' }
d1 = dict(d1)
print(dir(d1))
a = d1.get('first', 'xyz')
print(a)
print(d1.pop('first'))
print(d1)
d1.update(d)
print(d1)

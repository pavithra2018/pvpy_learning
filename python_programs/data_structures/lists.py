"""
 LIST :
     1. it is represented by []
     2. methods:
         a. append() # accepts only one argument. if want to pass multiple, make it a list and then pass
                     (o/p:reflects as list)
         b. extend() # accepts only one argument. if want to pass multiple, make it a list and then pass
                     (o/p:reflects as normal value)
         c. index() # this method searches for the element in the list.
                      it returns the index of first occurence of the element
         d. insert() # the insert() methods insert an object before the index provided.
         e. remove() # can remove the first occurence of an element
         f. pop()    # remove the last element of a list
         g. count()
         h. sort()
         i. reverse()
"""




lst = [1,2,3,1,4,1,5,6,7,5,8,9,10]
print(lst)
print(lst[0])
lst.append('good')
print(lst)
lst.append([11,12,13])
print(lst)
lst.extend(['girl',14,15])
print(lst)
print("5 is located in {}th index".format(lst.index(5)))
print(lst.index(1,3))
print(lst.index(5,3))
lst.insert(3,'bad')
print(lst)
lst.remove(5)
print(lst)
lst.pop()
print(lst)
print(lst.count(1))
lst1 = [4,5,2,3,6]
lst1.sort()
print(lst1) # default ascending order
lst1.sort(reverse=False)# ascendin order.......if reverse=True decending order
print(lst1)
lst1.reverse()
print(lst1)





class add():
    def __init__(self,a,b): 
        self.number1 = a 
        self.number2 = b  
    def add_them(self):
        self.total = self.number1 + self.number2
        return self.total
if __name__ == '__main__' :
    add_obj = add(10,30)
    print(add_obj.add_them())

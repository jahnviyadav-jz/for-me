class Employee : 
    a =1 

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name (self, value):
        self.fname = value.split("")[0]
        self.lname = value.split("")[1]

e = Employee()
e.name = 'Harry potter'
print(e.fname,e.lname)



#next concept operators overloading 
class Number : 
    def _init_(self,n): 
        self.n = n
    def _add_(self, num):
        return self.n + num.n 
    
n = Number(5)
m = Number(6)
print(n+m)

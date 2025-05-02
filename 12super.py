class Employee:
    def __init__(self):
        print("constructor of employee")
    a= 1

class Programmer(Employee):
    def _init(self):
        print("constructor of programmer")
    b= 2
        
class Manager(Programmer):
    def __init__(self):
        print("constructor of manager")
    c= 3


o = Employee() 
print(o.a) #output prints constructor of employee and 1
o = Programmer()
print(o.a) #output prints constructor of programmer and 2
o = Manager()
print(o.a) #output prints constructor of manager and 3

'''class Manager(programmer):
     def __init__(self):'
        super().__init__() 
        print("constructor of manager")'
        c= 3'
   agr hm super lga denge to ab 
   o = manager()'
    print(o.a) to ab constructor mei constructor of programmer '
    and constructor of manager dono print honge'''






#next topic 
class Employee: 
    a=1 
    def show(self):
        print(f "the class attribute of a is {self.a}")

e= Employee()
e.a = 45 
e.show() #output: the class attribute of a is 45
#but hame yaha pr class attribute chaiye to 
#so we write it like this 
class Employee:
    a=1 
    @classmethod 
    def show(cls):
        print(f"the class attribute of a is {cls.a}")
#tb ye directly class atrribute dikheaga 





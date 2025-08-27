#q1
class TwoDVector : 
    def __init__(self, i, j):
        self.i = i 
        self.j =j 

    def show(self): 
        print(f'the vector is {self.i}+ {self.j}j')

class ThreeDVector(TwoDVector): 
    def __init__(self, i, j, k):
        self.i = i 
        self.j = j 
        self.k = k 

    def show(self): 
        print(f'the vector is {self.i}+ {self.j}j + {self.k}k')

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(1, 2, 3)
b.show()


#q2
class Animals: 
    pass 
class Pets(Animals): 
    pass
class Dogs(Pets):
    @staticmethod
    def bark():
        print("Woof Woof") 

d = Dogs()
d.bark() #output: Woof Woof


#q3
class Employee: 
    salary = 234 
    increment = 20 
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary*(self.increment/100)
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100


e = Employee()
print(e.salaryAfterIncrement) #output: 280.8

e.salaryAfterIncrement = 280.8
print(e.increment) #output: 20.0


#q4
class Complex: 
    def_init_(self, r, i): 
        self.r =r 
        self.i =i 
    
    def _add_(self,c2):
        return complex(self.r + c2.r,self.i +c2.i )
    
    def_mul_(self,c2):
        real_part = self.r*c2.r - self.i*c2.i
        img_part = self.i*c2.r + self.r*c2.i
        return Complex(real_part, img_part)

    def __str__(self):
        return f"{self.r} + {self.i}i" #ye nhi likhte to hame addition shi se ni dikhta 


c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1+c2)
print(c1*c2) #output: -5 + 10i

#q5 
class Vector: 
    def_init_(self,x,y,z):
        self.x = x 
        self.y = y 
        self.z = z
    def _add_(self,other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    def_mul_(self,other):
        result = Vector(self.x * other.x + self.y * other.y + self.z * other.z)
        return result
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})" # or return f"{self.x}i + {self.y}j + {self.z}k"
    def_len_(self):
        return 3   #ese kr skte h and dusra tarika 

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)
print(v1+v2) #output: (5, 7, 9)
print(v1*v2) #output: 32


#q6
class Vector :
    def_init_(self,l):
        self.l = l 
    def_len_(self):
        return len(self.l)

 v1 = Vector([1, 2, 3])
print(len(v1)) #output: 3


        

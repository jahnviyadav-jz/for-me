class Employee:
    language = "Py" #this is a class attribute 
    salary = 1200000 #class attribute

    #init also called constructor 
    def __init__(self): #dunder method and it is automatically  called when we create an object of the class
        print("i am creating an obj")

    def getInfo(self):
        print(f'the lang is {self.language} and the salary is {self.salary}')
    
    @staticmethod #isme hme obj ki jarurat nahi hai islea staticmethod use kiya hai
    def greet():
        print("gm")


harry = Employee()
harry.name = "Harry" #this is an instance/object attribute
harry.language = "js" ####
print(harry.name,harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan roro robinson" #this is an instance/object attribute
print(rohan.name,rohan.salary, rohan.language)
#here name is instance attribute and salary and lang are class attributes as they directly belong to the class


harry.getInfo()
harry.greet()
#upper vala getinfo isme Employee.getInfo(harry) mei change hojayega islea bina self ke 
#error dikhega 


'''lets suppose we want to provide like this 
 harry =Employee('harry',1300000,'js')
toh hum constructor mei arguments pass karenge
toh hume __init__ mei arguments pass karne padenge
def __init__(self,name,salary,language):
self.name = name
self.salary = salary
self.language = language
print("i am creating an obj")'''
#and now hamne teno value pass ni ki to abb error ajeyga 

class Employee : 
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"the name of the Employee is {self.name} and the company  is {self.company}")

    
class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"the name of the Employee is {self.name}and the company  is {self.company}")

    def showLanguage(self):
        print(f"the name  is {self.company} and he is good with  {self.language}")


a = Employee()
b= Programmer()
print(a.company, b.company) # output = ITC ITC Infotech



## to hm copy n krne ki vjai inheritance ka istemal karenge 
class Programmer(Employee):#programmer class ko employee se inherrit krre h 
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name  is {self.company}and he is good with  {self.language} language ")




#multiple inheritance
class Coder: 
    language = "Python"
    def printLanguages(self):
        print(f'out of all the languages here is you language:{self.language}')

class Programmer(Employee,Coder):#multiple inheritance
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name  is {self.company}and he is good with  {self.language} language ")

 a = Employee()
b= Programmer()
b.showLanguage() #output: the name  is ITC Infotech and he is good with  Python language
b.printLanguage() #output: out of all the languages here is you language:Python
b.show() #output: the name of the Employee is Default name and the company  is ITC Infotech





#multilevel inheritace 
class Employee: 
    a= 1 
class Programmer(Employee): 
    b= 2
class Manager(programmer):
    c= 3
    
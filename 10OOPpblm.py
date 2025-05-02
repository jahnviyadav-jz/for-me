#q1 
class Programmer:
    company = "Microsoft"
    def __init__(self, name,  salary,ping):
        self.name = name
        self.salary = salary
        self.ping = ping

p = Programmer("Harry", 1200000, 245001)
print(p.name, p.salary, p.ping)
r = Programmer("Rohan", 1300000, 245001)
print(r.name, r.salary, r.ping)
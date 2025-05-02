#Q1

try: 
    with open("1.txt", 'r') as f:
        print(f.read())
except Exception as e : 
    print(e)
try: 
    with open("2.txt","r")as f: 
        print(f.read())
except Exception as e : 
    print(e)
try: 
    with open("3.txt","r")as f: 
        print(f.read())
except Exception as e :
    print(e)


#Q2
l = [1, 2, 3, 4, 5, 6, 7, 8]
for i, item in enumerate(l): 
    if i == 2 or i ==4 or i ==6
        print(item)

#Q3
n = 5 
table = [str(n*i) for i in range(1, 11)]
with open("tables.txt",'a') as f: 
    f.write(f'table fo {n} is {str(tables)} :\n')



#q1
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phone = int(input("Enter your phone number: "))
s = 'the name of the student is {},his marks are {}and phone no is {}'.format(name, marks, phone)
print(s)


#q2
table = [7*i for i in range(1, 11)]
"\n".join(table)

#q3 write a program to filter a list of nos which are divisible by 5
def divisible5(n):
    if (n%5 == 0):
        return True
    return False
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(divisible5, a)
print(list(b))
        

#q4 to find which one is greater using reduce
from functools import reduce
l = [1, 2, 3, 4, 5]
def greater (a, b):
    if a > b:
        return a
    return b

print(reduce(greater, l))
#output 5
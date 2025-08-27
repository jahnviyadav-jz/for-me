def myFun(): 
    print("hello world")

if __name__ == "__main__":
 #if this code is directly executed by running the file its present in 
    myFun()
    print(__name__)







##global 
x = 10  # Global variable

def change_x():
    global x  # Declaring x as global
    x = 20  # Modifies the global x
    print("Inside function:", x)

change_x()
print("Outside function:", x)
#output Inside function: 20
#Outside function: 20



#generally ese likhte h 
l = [1, 2, 3, 4, 5]
index= 0 
for item in l: 
    print(f"the item no at index {Index} is {item}")
    index+=1
#new way 
for index, item in enumerate(l):
    print(f"the item no at index {index} is {item}")




#general way 
myList = [1, 2, 3, 4, 5]
squareList = []
for item in myList:
    squareList.append(item *item)

print(squareList)

#new way (list comprehension)
squareList = [i*i for i in myList]



#
l= [1, 2, 3, 4, 5]
square = lambda x: x*x
sqList = map(square,l)
print(list(sqList))
#output [1, 4, 9, 16, 25]

#filter example 
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven= filter(even,l)
print(list(onlyEven))
#output [2, 4]

#reduce example 
from functools import reduce
def sum(a,b):
    return a+b
mul = lambda x,y : x*y

print(reduce(sum,l))
#output 15
print(reduce(mul,l))
#output 120


# terminal mei python -m venv jarvis 

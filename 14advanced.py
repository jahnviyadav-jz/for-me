#using walrus operator/assingment expression  
if (n := len([1,2,3,4,5])) > 3:
    print(f"list is too long ({n} elements k expected<=3)")


# 
n : int = 5 
name : str = "hello"
def sum(a: int, b: int)->int:
    return a + b


#
try: 
    a = int(input("hey enter a number: "))
    print(a)
except ValueError as v:
    print("heyyy")
    print(v)
except Exception as e:
    print( e)

print('thnku')

#
a = int(input("hey enter a number: "))
b = int(input("hey enter second  number: "))
if (b == 0):
    raise ZeroDivisionError("hey you cant divide by zero")
else:
    print(f"the division a/b is {a/b}")

#try else 
try: 
    a = int(input("hey enter a number: "))
    print(a)

except Exception as e:
    print( e)

else: 
    print("no exception was raised")
#when no error is raised else will run 

#try and finally 
try: 
    a = int(input("hey enter a number: "))
    print(a)

except Exception as e:
    print( e)
finally: 
    print("this will always run")
#and even if try returns it in def fn 
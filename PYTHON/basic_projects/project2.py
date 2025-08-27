#project 2 - the perfect guess 
import random 
n = random.randint(1,100)
a= -1
guesses = 0 
while a != n:
    a = int(input("guess the no :"))
    guesses += 1
    if (a>n):
        print("lower number please")
    elif(a<n):
        print("higher number please")
        
print(f"YOu have guessed the number {n} correctly in {guesses}attempts")  

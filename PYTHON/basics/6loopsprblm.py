#find the sum of first n natural nos 
n = int(input('enter the no :'))
sum = 0 
i = 1
while (i<n+1):
    sum += i 
    i += 1
print(sum)

#find factorail of a number 
n = int(input("enter the number : "))
product = 1 
for i in range(1,n+1):
    product = product*i 
print(product)


'''for n= 3 
  *
 ***
*****
'''
n = int(input('enter the no :'))
for i in range(1,n+1):
    print(" "*(n-i),end = "")
    print("*" *(2*i-1), end = "" )
    print("") #for new line  


''' *** 
    * *
    ***     for n=3'''
n = int(input("enter the no :"))
for i in range(1,n+1):
    if(i==1 or i==n):
       print("*"*n ,end="")
    else:
        print("*",end ="" )
        print(" "*(n-2),end= "")
        print("*",end = "")
    print("")  #for new line 


n = int(input('enter a number:'))
for i in range(1,11):
    print(f"{n}X{11-i} = {n*(11-i)}")

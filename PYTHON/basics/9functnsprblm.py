def f_to_c(f):
    return 5*(f-32)/9 

f = int(input('enter temperature in F'))
print(f_to_c(f)) 


print('a')
print('b')
print("c",end='') #end is equal to this to remove 
print("d",end='')#default new line in end 



def sum(n):
    if(n==1): 
        return  1 
    return n + sum(n-1)

print(sum(4))


'''***
   **  for n=3 
   * '''
def pattern(n):
    if(n==0): #ye lagana is necessary base condition 
        return # vrna infinite chlte rahega 
    print("*" * n )
    pattern(n-1)

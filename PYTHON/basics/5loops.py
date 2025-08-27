# for and while loop 
for i in range(1,6):
    print(i)
#while loop tabhi execute hoga jb condition tru ho 
while(i<6):
    print(i)
    i +=1 #i=i+1 


l = [1 ,'harry',false, 'this','rohan'] 
i = 0 
while (i<len(l)):
    print(l[i])
    i += 1 


#for and else
 l = [ 1,7,8]
for item in l : 
    print(item)
else : 
    print("done")#else will work when for loop ends 


n = int(input("enter a number: "))
for i in range (1,11): 
    print(f"{n} X {i} = {n*i}")

#normally ese likhte hai 
f = open("7files.txt")
print(f.read())
f.close()

#the same can be written using with statement 
with open ("7files.txt") as f :
    print (f.read() )  
#no need to close in this auto close hojata hai jb hm with se bahr niklte hai 
 

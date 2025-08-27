''' a = " a very long string with emails " 
emails = [] emails agye is list mei after running code but ye emails kahi store nhi honge 
thats why we are using files 
pr'''

f = open("7files.txt","r")
data = f.read()
print(data)
f.close() 


st = 'hey you are amazing '
f = open('8files.txt','w')
f.write(st)
f.close 


f = open("7files.txt")
lines = f.readlines()#lines ko list ki form mei dedega  
print(lines, type(lines))


#readline tb tk read krti rahti h jb tk uske pass empty string n ajjae
line1 = f.readline()
print( line1 ,type(line1))
line2 = f.readline()
print( line2 , type(line2))
line3 = f.readline()
print( line3 , type(line3)) 
line4 = f.readline()
print( line4  == "")

#loop se karenge to 
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
 
f.close()

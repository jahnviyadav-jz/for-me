#python add automatic space if we are using comma in btw 
''' if 
elif 
elif 
else 
then if any one condition from starts holds tru then vo execute hoke program end hojayega no need to check other conditions '''


#case of two iffs #both if alag alag chalenge 

a = int(input("enter your age : "))
#if stament 1 
if(a%2 ==0 ) : 
    print("a is even ")

#if statement 2 
if(a>=18):
    print("you are above the age of conssent")
    print('good for you')
elif(a<0):
    print('you are entering an invalid negative age')
else:
    print('you are below the age of consent')
print('end of program')
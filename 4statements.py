'''ye agr break nhi hota to value 99 tk print krta per break ka mtlb pr is
case mei ye jese hi value 34 hui to ye loop se turant exit hojayega and value
33 tk hi print hogi 
'''
for i in range(100) : 
    if(i == 34) : 
        break 
    print(i)
for i in range(100) : 
    if(i == 34) : 
        continue #it only skips this iteration means it doesnt print 34 skips it 
               #nd jumps to 35 then goes normal 
    print(i)


for i in range(645): 
    pass #it instructs to do nothing so with this we can come back later if 
         #we want to write anything or just skips it for testing further program 

i = 0 
while(i<45): 
    print(i)
    i+= 1 
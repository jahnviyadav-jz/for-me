#when harry2 is not in the dict 
print(marks.get("harry2"))#prints none 
print(marks["harry2"])#returns an error

empty dict = {}
empty set =set()


s= set()
s.add(20)
s.add(20.0)"""it shows length of set as 1 it is considering both as equlas 
1==1.0 is tru in python """


import pyjokes
joke = pyjokes.get_joke()
print(joke)
#shortcut key for making a comment is control + Forward slash 




b= int (input( 'enter a number : '))
b= int (input( 'enter a number : '))  

name = "yadav"  
print(name[0:5]) #str slicing 
print(name[:5])  #valid 
print(name[0:]) #valid . for making negative slicing easier you can first convert then in positive slicing 
print(name[1:4:2])# end thing is skip only pick 2nd element from given range 



marks = []  #double click to select and change all occurances option after right click 
f1 = input("enter marks obtained  : ")
marks.append(f1)
f2 = input("enter marks obtained : " )
marks.append(f2)
f3 = input("enter marks obtained : " )
marks.append(f3)
f4 = input("enter marks obtained : " )
marks.append(f4)
marks.sort()
print(marks)  



name = input('enter your name : ')
print('good morning ', name ) 

#imp new thing 
print(f'good morning {name }')

letter = ''' Dear <|Name|>,
You are selected!
 <|Date|>'''
print(letter.replace("<|Name|>" ," Harry").replace("<|Date|>","24 sep 24" ))

fruits = []
f1 = input("enter fruit name : ")
fruits.append(f1)
f2 = input("enter fruit name: " )
fruits.append(f2)
f3 = input("enter fruit name: " )
fruits.append(f3)
f4 = input("enter fruit name: " )
fruits.append(f4)
f5 = input("enter fruit name: " )
fruits.append(f5)
f6 = input("enter fruit name: " )
fruits.append(f6)
f7 = input("enter fruit name: " )
fruits.append(f7)
f8 = input("enter fruit name: " )
fruits.append(f8)
print(fruits)   #can move the whole slected thing up and down by alt +arrow 
                #alt+shift +downward arrow to duplicate selected thing 



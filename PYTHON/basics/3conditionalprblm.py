a1 = int(input('enter no 1 :'))
a2 = int(input('enter no 2 :'))
a3= int (input('enter no 3:'))
a4= int (input('enter no 4:'))
if(a1>a2 and a1>a3 and a1>a4 ) :
        print("greatest no is a1 :", a1)
if(a2>a1 and a2>a3 and a2>a4 ) :
        print("greatest no is a2 :", a2)
if(a3>a1 and a3>a2 and a3>a4 ) :
        print("greatest no is a3 :", a3)
if(a4>a1 and a4>a2 and a4>a3 ) :
        print("greatest no is a4 :", a4)
          


sub1 = int(input('Enter marks of sub1: '))
sub2 = int(input('Enter marks of sub2: '))
sub3 = int(input('Enter marks of sub3: '))

# Calculate percentage
percentage = ((sub1 + sub2 + sub3) / 300) * 100

# Check percentage and individual marks
if percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print('Pass')
else:
    print('Fail')



p1 = '“Make a lot of money”
p2 = 'buy now'
p3 =  'subscribe this' 
p4 = 'click this'
message = input("enter a commment :")
if ((p1 in message )or (p2 in message) or (p3 in message) or (p4 in message)) :
    print("spam comment ")
else : 
    print('this comment is not a spam')

# in can also be used for to check if this word is in list or not 




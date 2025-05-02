#logic ko ek naam dedo is functions 
#functions with arguments 
def goodday( name , ending):
    print('good day,' + name )
    print(ending)
    return 'ok'
    
a = goodday('harry','thank you')
print(a)


 #recursion (fn which calls it itself)
 def factorial(n) : 
   if(n==1 or n==0) :
     return 1 
   return n*factorial(n-1)

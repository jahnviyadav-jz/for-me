#Q1
f = open("poem.txt")
content= f.read()
if('twinkle' in content):
    print( "present ")
else:
    print('not present')
f.close()

#Q2
import random 
def game():
    print("you are playing the game...")
    score = random.randint(1,62)
    #fetch the hiscore 
    with open("Hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore = int(hiscore)
        else:
            hiscore=0 

    print(f"your score:{score}")
    if(score>hiscore):
        #write this hiscore to the file 
        with open("Hiscore.txt",'w') as f :
            f.write(str(score))

    return score 

game() 


#Q3
def generateTable(n):
    table = ""
    for i in range (1,11): 
        table += f'{n}X{i}={n*i}\n'
    
    with open(f"tables/table_{n}.txt","w") as f : 
        f.write(table)

for i in range (2,11):
    generateTable(i)

#Q4
with open("poem.txt") as f: 
    content = f.read()
    newcontent = content.replace("donkey",'####')
with open("poem.txt","w") as f:
    f.write(newcontent)


#Q5
words = ["donkey","gadha"]
with open("poem.txt") as f: 
    content = f.read()
for word in words : 
    content  = content.replace(word, "#"*len(word))
with open("poem.txt","w") as f:
    f.write(content)

#Q6
with open("log.txt") as f :
    content= f.read()

if("python" in content):
    print("yes present")
else : 
    print("not present ")

#Q7  
with open(log.txt) as f:
    lines = f.readlines()

lineno = 1 
for line in lines:
    if ("python" in line): 
        print(f"yes python is present. line no : {lineno}")
         break
    lineno += 1 
else:
    print("no pythob is not present")

#Q8
with open("this.txt") as f: 
    content = f.read()

with open ("this_copy.txt","w") as f:
    f.write(content)

#Q9 
with open("file1.txt") as f: 
    content1 = f.read()
with open("file2.txt") as f:
    content2 = f.read()
if(content1 == content2):
    print("same")
else:
    print("not same")

#Q10 
with open("this.txt",'w') as f:
    f.write("")  ## to wipe the content of the file 
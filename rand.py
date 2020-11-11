import random


f=open('what','r',encoding='UTF-8')

lines=f.readlines()

x=random.randint(0,len(lines)-1)
print(lines[x])

f.close()



f=open('names','r',encoding='UTF-8')

lines=f.readlines()

x=random.randint(0,len(lines)-1)
print(lines[x])

f.close()
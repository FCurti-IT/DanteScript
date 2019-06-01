import random

def terzina():
   f = open('dante.txt','r')
   lines = f.readlines()
   partenza = random.randrange(20,len(lines)-3)

   while lines[partenza] != '\n' or lines[partenza+4] != '\n' or lines[partenza+1] == '\n' or lines[partenza+2] == '\n' or lines[partenza+3] == '\n':
      partenza = partenza-1
   
   return '.\n'+lines[partenza+1]+lines[partenza+2]+lines[partenza+3] 
   #print(lines[partenza+1])
   #print(lines[partenza+2])
   #print(lines[partenza+3])


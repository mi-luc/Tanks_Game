import time
import math, pygame,sys,random
import numpy as np
pygame.init()
width=1300
height=800
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("GRAV2")

def planet(x,y,color,th):
    pygame.draw.circle(win,color,(x,height-y),th)

def rand(a,b):
    current_time = time.time()
    dif=abs(b-a)
    current_time/=1000
    current_time**=2
    print(current_time)
    timp=int(current_time)
    random=timp%(dif)
    return random+a
a=0
b=10
perc=[]
"""for i in range(b-a):
    perc.append(0)
for i in range(10000000):
    index=rand(a,b)
    perc[index]+=1
summ=0
for i in range(b-a):
    perc[i]/=100000
    summ+=perc[i]
    print(i,perc[i])
print(summ)"""
run=True 

while run:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run=False
    keys= pygame.key.get_pressed()
    if keys[pygame.K_e]:
        x=rand(1,1300)
        y=rand(0,800)
        planet(x,y,(200,100,50),5)
    pygame.display.update() 
        
        
pygame.quit()
sys.exit()
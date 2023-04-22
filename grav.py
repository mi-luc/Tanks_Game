import math
import random
import pygame
import numpy as np
import sys
pygame.init()
width=1000
height=600
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Raycasting")

start=True
angle1=0
angle2=0
force=0
R=0
mass1=100
mass2=100
x1=390
y1=100
x2=400
y2=500
v1x=0.1
v1y=0.3
v2x=-0.1
v2y=0
FPS=200
fpsClock = pygame.time.Clock()
while start:
    fpsClock.tick(FPS)
    win.fill((20,20,20))
    R=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if R==0:
           R=0.0001
    force= mass1*mass2/R**2
    dif=x2-x1
    if y2-y1>0:
        angle1=math.atan((y2-y1)/(dif))
        while angle1<0:
            angle1+=3.1415926
            #print("DA")
        angle2=angle1
        angle1+=3.1415926
    if y2-y1<0:
        angle1=math.atan((y1-y2)/(dif))
        while angle1<0:
            angle1+=3.1415926
            #print("DA")
        angle2=angle1
        angle1+=3.1415926
     
    print(np.rad2deg(angle1),np.rad2deg(angle2),angle1)
    pygame.draw.circle(win,(255,250,250),(x1,y1),6)
    pygame.draw.circle(win,(50,200,50),(x2,y2),8)
    a1_x=force/mass1*math.cos(angle2)
    a2_x=force/mass2*math.cos(angle1)
    a1_y=force/mass1*math.sin(angle2)
    a2_y=force/mass2*math.sin(angle1) 
    #print(force,R)
    #print(force)
    #print(a1_x,a1_y,np.rad2deg(angle1),np.rad2deg(angle2))
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            start=False
    pygame.display.update() 
    x1+=v1x
    x2+=v2x
    y1+=v1y
    y2+=v2y
    v1x+=a1_x
    v1y+=a1_y
    v2x+=a2_x
    v2y+=a2_y
    
    
    
        
pygame.quit()
sys.exit()
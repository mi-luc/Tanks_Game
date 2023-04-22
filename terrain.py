import math
import random
import pygame
import numpy as np
from PIL import Image
k1=[]
k4=[]
pixel1 = pygame.image.load('grass1.png')
pixel2= pygame.image.load('grass2.png')
pixel3 = pygame.image.load('grass3.png')
pixel4 = pygame.image.load('mud.png')
pixel5 = pygame.image.load('rock.png')

def rand_terrain(width):
     k5=random.random()
     if k5<0.5:
         k5=1
     else:
         k5=-1
     k2=-1
     k3=-1
     while k2<0.04 or k2>0.06: 
         k2=random.random()
     while k3<40 or k3>110:
         k3=random.random()*90
     for i in range(width):
         k1.append(random.random())
         k4.append((i/400)**6-((i/500)+1)**5+((i/200)+1)**3-(i/80)**2)
     inaltime=[]
     i=0
     trench=random.randint(100,900)
     hill=random.randint(100,900)
     #print(k2,k3,k5)
     while i<width:
      #inaltime.append(200+k3*math.sin((i/10)*k2)+k6*k1[i]+k5*k4[i]+80*math.sin(0.02*(i/5)+50))
      inaltime.append(200+k3*math.sin((i/3)*k2)+k5*k4[i]+math.sin(0.1*(i/2))+10*10**(-(i-hill)*(i-hill)/100000+1.25)-5*5**(-(i-trench)*(i-trench)/100000+1))
      i+=1
     return inaltime

def pixel_draw(win,inaltime,height,width):
  i=0
  while i<width:
     y=inaltime[i]
     y=int(y)
     for j in range(y):
       if j<=y and j>y-10:
         win.blit(pixel1,(i,height-j))
       if j<=y-10 and j>y-40:
         win.blit(pixel2,(i,height-j))
       if j<=y-40 and j>y-100:
         win.blit(pixel3,(i,height-j))
       if j<=y-100 and j>y-200:
         win.blit(pixel4,(i,height-j))
       if j<=y-200:
         win.blit(pixel5,(i,height-j))        
     i+=1
     
def terrain_photo(inaltime,number,width,height,level):
  data = np.zeros((height, width, 3), dtype=np.uint8)
  sir='my'
  if level==1:
   for j in range(width):
    i=0
    while i<height:
     if i>inaltime[j]:
      k=random.randint(0,1000)
      if k>=998:
          data[height-i-1][j]=(255,255,255)
      else:  
         data[height-i-1][j]=(71,60,105)
     if i<=inaltime[j]:
      data[height-i-1][j]=(51, 204, 51)
     if i<=inaltime[j]-200:
      data[height-i-1][j]=(255, 204, 102)
     i+=1
  if level==2:
   for j in range(width):
    i=0
    while i<height:
     if i>inaltime[j]:
      k=random.randint(0,1000)
      if k>=998:
          data[height-i-1][j]=(255,255,255)
      else:  
         data[height-i-1][j]=(196, 77, 255)
     if i<=inaltime[j]:
      data[height-i-1][j]=(255, 92, 51)
     if i<=inaltime[j]-200:
      data[height-i-1][j]=(255, 92, 102)
     i+=1
  if level==3:
   for j in range(width):
    i=0
    while i<height:
     if i>inaltime[j]:
      k=random.randint(0,1000)
      if k>=998:
          data[height-i-1][j]=(255,255,255)
      else:  
         data[height-i-1][j]=(255, 83, 26)
     if i<=inaltime[j]:
      data[height-i-1][j]=(51, 205, 204)
     if i<=inaltime[j]-200:
      data[height-i-1][j]=(100, 205, 180)
     i+=1
  if level==4:
   for j in range(width):
    i=0
    while i<height:
     if i>inaltime[j]:
      k=random.randint(0,1000)
      if k>=997:
          data[height-i-1][j]=(255,255,255)
      else:  
         data[height-i-1][j]=(0, 0, 0)
     if i<=inaltime[j]:
      data[height-i-1][j]=(128, 128, 128)
     if i<=inaltime[j]-200:
      data[height-i-1][j]=(142, 128, 159)
    
     i+=1
  img1 = Image.fromarray(data, 'RGB')
  img1.save(sir+str(number)+'.png')  
  return data,sir+str(number)+'.png'

def remake_photo(inaltime,data,width,height,level,x,y,number):
  sir='my'
  nr=0
  Radius=random.randint(10,15)
  for i in range(2*Radius):
      #angle=math.radians(i*3)
      nr1=2*math.sqrt(Radius**2-(i-Radius)**2)
      nr=int(nr1)
      for j in range(nr):
           k=random.randint(0,1000)
           if x+j-nr//2<width and x+j-nr//2>0 and level==1 and height-(y+i-Radius)<550:
            if data[height-(y+i-Radius)][x+j-nr//2][1] == 204:
                inaltime[x+j-nr//2]-=1
            data[height-(y+i-Radius)][x+j-nr//2]=(71,60,105)
            if k>=998:
                data[height-(y+i-Radius)][x+j-nr//2]=(255,255,255)
           elif  x+j-nr//2<width and x+j-nr//2>0 and level==2 and height-(y+i-Radius)<550:
                if data[height-(y+i-Radius)][x+j-nr//2][1] == 92:
                   inaltime[x+j-nr//2]-=1
                data[height-(y+i-Radius)][x+j-nr//2]=(196, 77, 255)
                if k>=998:
                 data[height-(y+i-Radius)][x+j-nr//2]=(255,255,255)
           elif x+j-nr//2<width and x+j-nr//2>0 and  level==3 and height-(y+i-Radius)<550:
               if data[height-(y+i-Radius)][x+j-nr//2][1] == 205:
                   inaltime[x+j-nr//2]-=1
               data[height-(y+i-Radius)][x+j-nr//2]=(255, 83, 26)
               if k>=998:
                data[height-(y+i-Radius)][x+j-nr//2]=(255,255,255)
           elif x+j-nr//2<width and x+j-nr//2>0 and  level==4 and height-(y+i-Radius)<550:
               if data[height-(y+i-Radius)][x+j-nr//2][1] == 128:
                   inaltime[x+j-nr//2]-=1
               data[height-(y+i-Radius)][x+j-nr//2]=(0, 0, 0)
               if k>=996:
                data[height-(y+i-Radius)][x+j-nr//2]=(255,255,255)

  for i in range(2*Radius):
            numara=0
            for j in range(100):
                k=random.randint(0,1000)
                if level==1 and data[height-(y+j-Radius)][x-Radius+i][2]==51:
                    data[height-(y+j-Radius)][x-Radius+i]=(71,60,105)
                    if k>=998:
                        data[height-(y+numara-Radius)][x-Radius+i]=(255,255,255)
                    else: 
                        data[height-(y+numara-Radius)][x-Radius+i]=(51, 204, 51)
                    numara+=1
                if level==1 and data[height-(y+j-Radius)][x-Radius+i][2]==102:
                    data[height-(y+j-Radius)][x-Radius+i]=(71,60,105)
                    data[height-(y+numara-Radius)][x-Radius+i]=(255, 204, 102)
                    if k>=998:
                        data[height-(y+numara-Radius)][x-Radius+i]=(255,255,255)
                    else: 
                        data[height-(y+numara-Radius)][x-Radius+i]=(51, 204, 51)
                    numara+=1
                    
           
  img1 = Image.fromarray(data, 'RGB')
  img1.save(sir+str(number)+'.png')  
  return data,sir+str(number)+'.png',inaltime
def display_acc(win,level):
    font=pygame.font.SysFont('bahnschrift',20)
    if level==1:
        txt1= font.render("Pamant Acceleratia gravitationala=1g",True,(51, 204, 51))
        win.blit(txt1,(300,20))
    if level==2:
        txt1= font.render("Venus Acceleratia gravitationala<1g",True,(255, 92, 51))
        win.blit(txt1,(300,20))
    if level==3:
        txt1= font.render("Neptun Acceleratia gravitationala>1g",True,(51, 205, 204))
        win.blit(txt1,(300,20))
    if level==4:
        txt1= font.render("Spatiu Acceleratia gravitationala<<1g",True,(128, 128, 128))
        win.blit(txt1,(300,20))
        
    
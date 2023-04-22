import math, pygame,sys,random
import numpy as np
pygame.init()
width=1300
height=800
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("GRAV2")

NR=2
cord=np.array([[500.0,500],[500,600.0]])
speed_angle=np.array([[0.0,1],[0.0,0]])
a_angle=np.array([0.0,0.0])
FPS=500
m1=50000
m2=10
def planet(x,y,color,th):
    pygame.draw.circle(win,color,(x,height-y),th)

def hit(x,y,i):
   if x<0.5:
       speed_angle[0][i]*=-1
   if y<0.5:
       speed_angle[1][i]*=-1
   if x>width-1:
       speed_angle[0][i]*=-1
   if y>height-1:
       speed_angle[1][i]*=-1
def friction():
  ab=0  
fpsClock = pygame.time.Clock()
run=True
win.fill((20,20,20))
while run:
           
    #print(cord)
    x1=float(cord[0][0])
    x2=float(cord[0][1])
    y1=float(cord[1][0])
    y2=float(cord[1][1])
    fpsClock.tick(FPS)
    hit(cord[0][0],cord[1][0],0)
    hit(cord[0][1],cord[1][1],1)
    keys= pygame.key.get_pressed()
    if keys[pygame.K_e]:
        cord[0][0]=random.randint(0,1300)
        cord[0][1]=random.randint(0,600)
        cord[1][0]=random.randint(0,1300)
        cord[1][1]=random.randint(0,600)
        speed_angle[0][0]=random.randint(0,10000)/100000
        speed_angle[0][1]=random.randint(0,10000)/100000
        speed_angle[1][0]=random.randint(0,10000)/100000
        speed_angle[1][1]=random.randint(0,10000)/100000
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run=False
    for k in range(NR):
        planet(cord[0][k],cord[1][k],(200,200,200),2)
    pygame.display.update() 
    for k in range(NR):
        cord[0][k]+=speed_angle[0][k]
        cord[1][k]+=speed_angle[1][k]
    if math.sqrt((x1-x2)**2+(y1-y2)**2)<10:
        R=10
    else:
        R=math.sqrt((x1-x2)**2+(y1-y2)**2)
  
    F=m1*m2/R**2*0.003
    a1=F/m1
    a2=F/m2
    a_angle[0]=abs((x2-x1))
    a_angle[1]=abs((y2-y1))
    if a_angle[0]<2:
        a_angle[0]=2
    tan=a_angle[1]/a_angle[0]
    unghi=math.atan(tan)
    #print(speed_angle,a1,a2,unghi*180/3.141,x1,y1)
    i=0
    
    if x2-x1>0:
        speed_angle[0][0]+=math.cos(unghi)*a1
    else:
        speed_angle[0][0]-=math.cos(unghi)*a1
    if y2-y1>0:
        speed_angle[1][0]+=math.sin(unghi)*a1
    else:
        speed_angle[1][0]-=math.sin(unghi)*a1
    i=1
    if x1-x2>0:
        speed_angle[0][1]+=math.cos(unghi)*a2
    else:
        speed_angle[0][1]-=math.cos(unghi)*a2
    if y1-y2>0:
        speed_angle[1][1]+=math.sin(unghi)*a2
    else:
        speed_angle[1][1]-=math.sin(unghi)*a2
        
pygame.quit()
sys.exit()
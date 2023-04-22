import random
import pygame
import math
import terrain, fuel, force_angle,play, bullet,life,cheat
import sys
from PIL import Image
import numpy as np

####################################SCREEN
pygame.init()
width=1000
height=600
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Tanks")
icon=pygame.image.load('explosion.png')
pygame.display.set_icon(icon)
#############################################

###TERRAIN
###PRIMA VERSIUNE
def rand_terrain(width=1000):
 global inaltime
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
 while i<width:
  #inaltime.append(200+k3*math.sin((i/10)*k2)+k6*k1[i]+k5*k4[i]+80*math.sin(0.02*(i/5)+50))
  inaltime.append(200+k3*math.sin((i/3)*k2)+k5*k4[i]+math.sin(0.1*(i/2))+10*10**(-(i-hill)*(i-hill)/100000+1.25)-5*10**(-(i-trench)*(i-trench)/100000+1))
  i+=1

pixel1 = pygame.image.load('grass1.png')
pixel2=pygame.image.load('grass2.png')
pixel3 = pygame.image.load('grass3.png')
pixel4 = pygame.image.load('mud.png')
pixel5 = pygame.image.load('rock.png')
k1=[]
k4=[]
hit_terrain=[]
##################################################
##################################################
#BUTTON
#Nu mai am nevoie
def text_objects(text, font,color):
    textSurface = font.render(text, True, (100,0,100))
    return textSurface, textSurface.get_rect()
  
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",10)
    textSurf, textRect = text_objects(msg, smallText,(0,0,0))
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)
    
##################################################
#General


    
##################################################
###PLAYER
playX=100
playY=0
fuel_player=100
force_player=20
viata1=100
player_angle_bullet=30
##################################################
###ENEMY
enX=width-100
enY=0
fuel_enemy=100
viata2=100
force_enemy=20
cheating=False
enemy_angle_bullet=150
##################################################
NR_cans=random. randint(2,5)
Xlist=[]
Xlist=fuel.spawnfuel(NR_cans,width)
####################################################
################versiune veche
def crater(x,y):
  global hit_terrain
  copy=x
  R=random.randint(10,20)
  x-=R
  i=0
  ok=0
  while x<copy+R:
    if x>0 and x<width:
      hit_terrain[int(x)]-=i
    if i<R:
      i+=1
    if i==R:
      ok=1
    if ok==1:
      i-=1
    x+=1
      
#################################################
###Impusca glontul, versiunea veche
img_bullet=pygame.image.load('circle.png')
prop1=1
factor=10
def fire_bullet(player,force,angle):
  angle*=3.141/180
  global playX
  global playY
  global enX
  global enY
  global inaltime
  if player==1:
     bulX=playX
     bulY=playY-5
     factor=force/2
     prop1=0.5
     prop2=0.001
     factorX=factor*math.cos(angle)
     factorY=factor*math.sin(angle)
     while bulY<=height-inaltime[int(bulX)] and bulX>1 and bulX<width-10:
      clock.tick(30)
      pygame.display.update()
      pygame.draw.circle(win, (0,0,0), (int(bulX), int(bulY)), 2, 2)
      #win.blit(img_bullet,(int(bulX),int(bulY)))
      bulX+=factorX
      bulY-=factorY
      factorY-=prop1
      prop1-=prop2
      pygame.display.update()
  return bulX
##################################################


start=True
meniu=True
running=True

X_change=0
inaltime=terrain.rand_terrain(width)
runda=random.randint(1,2)
fire=0
wait=0


x=random.randint(0,width-550)
y=random.randint(0,height-50)
k1=1
k2=1
count=0
level=0
meniu_font=pygame.font.SysFont('bahnschrift',50)
txt_alege=pygame.font.SysFont('bahnschrift',23)
txt=txt_alege.render('Alege harta pe care vrei sa joci:',True,(0,0,0))
txt1= meniu_font.render('1',True,(0,0,0))
txt2= meniu_font.render('2',True,(0,0,0))
txt3= meniu_font.render('3',True,(0,0,0))
txt4= meniu_font.render('4',True,(255,255,255))
poza_meniu=pygame.image.load('load.png')
pamant=pygame.image.load('earth.jpg')
venus=pygame.image.load('venus.jpg')
neptun=pygame.image.load('neptun.jpg')
space=pygame.image.load('space.jpg')
#############################################################################
menu_font=pygame.font.SysFont('bahnschrift',50)
font=pygame.font.SysFont('bahnschrift',20)
keys= pygame.key.get_pressed()


#################################################Primul meniu
while start:
  """
  R=random.randint(-10,0)
  G=random.randint(-10,0)
  B=random.randint(-10,0)
  """
  B=random.randint(-50,0)
  menu_color=(255,255,255+B)
  txt_cheat=font.render('Press "N"/"Y" to de/activate cheats:',True,(108,108,108))
  txt_no=font.render('No',True,(108,108,108))
  txt_yes=font.render('Yes',True,(108,108,108))
  menu_text= menu_font.render('PRESS ENTER TO START:',True,menu_color)
  menu_photo=pygame.image.load('tancuri.jpg')
  for event in pygame.event.get():
    if event.type is pygame.QUIT:
      start=False
      running=False
      meniu=False
  keys= pygame.key.get_pressed()
  if keys[pygame.K_RETURN]:
    start=False
  x+=k1
  y+=k2
  if x==width-550:
      k1=-1
  if x==0:
      k1=1
  if y==height-50:
      k2=-1
  if y==0:
      k2=1
  win.blit(menu_photo,(0,0))
  win.blit(txt_cheat,(50,50))
  if keys[pygame.K_y]:
      cheating=True
  if keys[pygame.K_n]:
      cheating=False
  if cheating==False:
     win.blit(txt_no,(375,50))
  else:
     win.blit(txt_yes,(375,50))
  win.blit(menu_text,(x,y))
  pygame.display.update()
##################################################################################

##################################################Al doilea meniu
afisaj=0
while meniu==True:
    win.blit(pamant,(0,0))
    win.blit(venus,(width//3,0))
    win.blit(neptun,(2*width//3,0))
    win.blit(space,(0,400))
    win.blit(txt1,(70,200))
    win.blit(txt2,(400,200))
    win.blit(txt3,(730,200))
    win.blit(txt4,(450,500))
    afisaj+=1
    if afisaj<300:
        win.blit(txt,(2,20))
    if afisaj==450:
        afisaj=0
    for event in pygame.event.get():
     if event.type is pygame.QUIT:
      meniu=False
      running=False
    keys= pygame.key.get_pressed()
    if keys[pygame.K_1]:
     meniu=False
     level=1
    if keys[pygame.K_2]:
     meniu=False
     level=2
    if keys[pygame.K_3]:
     meniu=False
     level=3
    if keys[pygame.K_4]:
     meniu=False
     level=4
    pygame.display.update()
##################################################
load=pygame.image.load('load.png')
data = np.zeros((height, width, 3), dtype=np.uint8)
nume_poza=''
win.blit(load,(-50,-200))
pygame.display.update()
data,nume_poza=terrain.terrain_photo(inaltime,level,width,height,level)
img1=pygame.image.load(nume_poza)
######################################################
bullet_type=1

##################################################   

clock = pygame.time.Clock()
while running:
  new_p=0
  clock.tick(20)
 ###############################################################################################PLAYER AND ENEMY 
  #terrain.pixel_draw(win,inaltime,height,width)
  win.blit(img1,(0,0))
  terrain.display_acc(win,level)
  play.player(enX,enY,height,inaltime,win,0)
  enX_change=0
  play.player(playX,playY,height,inaltime,win,1)
  X_change=0
  if wait==0:
   life.print_life(viata1,60,30,win)
   life.print_life(viata2,940,30,win)
###############################################################################################FUEL  
  fuel.show_cans(Xlist,height,inaltime,win)
  if fuel_player<0:
    fuel_player=0
  if fuel_enemy<0:
    fuel_enemy=0
  if wait==0: 
   fuel.display_fuel(win,fuel_player,20,550,)
   fuel.display_fuel(win,fuel_enemy,780,550,)
   fuel_player+=fuel.get_fuel(fuel_player,playX,Xlist)
   if fuel_player>100:
       fuel_player=100
   Xlist=fuel.update_list(fuel_player,playX,Xlist)
   fuel_enemy+=fuel.get_fuel(fuel_enemy,enX,Xlist)
   if fuel_enemy>100:
       fuel_enemy=100
   Xlist=fuel.update_list(fuel_enemy,enX,Xlist)
###############################################################################################
  
  keys= pygame.key.get_pressed()
  #player_angle_bullet=get_angle(player_angle_bullet,70,520,keys,1)
  if runda==1 and wait==0:
   force_angle.traj_angle(player_angle_bullet,win,playX,playY,force_player,70,530,runda)
   if keys[pygame.K_c] and cheating==True:
    cheat.get_force(win,playX,playY,enX,enY,player_angle_bullet,width,inaltime,height,level)
   if keys[pygame.K_i]:
    player_angle_bullet+=2
   if keys[pygame.K_k]:
     player_angle_bullet-=1
   if keys[pygame.K_u]:
    force_player-=1
   if keys[pygame.K_o]:
     force_player+=2
   if force_player<=1:
     force_player=2
   if player_angle_bullet<=-40:
     player_angle_bullet=-40
   if player_angle_bullet>=220:
      player_angle_bullet=220
   if force_player>=40:
     force_player=40
   if keys[pygame.K_SPACE]:
     fire=1
  elif runda==2 and wait==0:
   force_angle.traj_angle(enemy_angle_bullet,win,enX,enY,force_enemy,835,530,runda)
   if keys[pygame.K_c] and cheating == True:
    cheat.get_force(win,enX,enY,playX,playY,enemy_angle_bullet,width,inaltime,height,level)
   if keys[pygame.K_k]:
    enemy_angle_bullet+=1
   if keys[pygame.K_i]:
     enemy_angle_bullet-=2
   if keys[pygame.K_u]:
    force_enemy-=1
   if keys[pygame.K_o]:
     force_enemy+=2
   if force_enemy<=1:
     force_enemy=2
   if enemy_angle_bullet<=-40:
     enemy_angle_bullet=-40
   if enemy_angle_bullet>=220:
      enemy_angle_bullet=220
   if force_enemy>=40:
     force_enemy=40
   if keys[pygame.K_SPACE]:
     fire=2

###############################################################EXPLOSION, PIERDE VIATA
#######PLAYER 1
  font=pygame.font.SysFont('bahnschrift',20)     
  if keys[pygame.K_1]:
      bullet_type=1
      txt_bullet= font.render("Proiectil normal",True,(0,255,255))
      win.blit(txt_bullet,(350,550))
  elif keys[pygame.K_2]:
      bullet_type=2
      txt_bullet= font.render("Racheta ghidata",True,(0,255,255))
      win.blit(txt_bullet,(350,550))
  #elif keys[pygame.K_3]:
   #   bullet_type=3
  if fire==1 and wait==0:
    if bullet_type==1:
        explodeX1=bullet.fire_bullet(playX,playY,force_player*1.3,player_angle_bullet,inaltime,win,height,width,level)
    if bullet_type==2:
        explodeX1=bullet.fire_rocket(playX,playY,player_angle_bullet,inaltime,win,height,width,level,enX,enY,1)
    x1=1
    x1=int(explodeX1)
    if x1>30 and x1<width-30:
     y1=int(inaltime[x1])
     data,nume_poza,inaltime=terrain.remake_photo(inaltime,data,width,height,level,x1,y1,level)
     img1=pygame.image.load(nume_poza)
    dif1=abs(enX-explodeX1)
    dif1=int(dif1)
    if dif1<50 and bullet_type==1: 
        viata2-=50-dif1-random.randint(5,15)
     #viata2=math.floor(viata2)
    if bullet_type==2:
        viata2-=random.randint(5,20)
    fire=0
    runda=2
    wait=1
 #######PLAYER 2 
  if fire==2 and wait==0:
    if bullet_type==1:  
        explodeX2=bullet.fire_bullet(enX,enY,force_enemy*1.3,enemy_angle_bullet,inaltime,win,height,width,level)
    if bullet_type==2:
        explodeX2=bullet.fire_rocket(enX,enY,enemy_angle_bullet,inaltime,win,height,width,level,playX,playY,2)
    x1=1
    x1=int(explodeX2)
    if x1>30 and x1<width-30:
     y1=int(inaltime[x1])
     data,nume_poza,inaltime=terrain.remake_photo(inaltime,data,width,height,level,x1,y1,level)
     img1=pygame.image.load(nume_poza)
    dif2=abs(playX-explodeX2)
    dif2=int(dif2)
    if dif2<50 and bullet_type==1:
        viata1-=50-dif2-random.randint(5,15)
        #viata1=math.floor(viata1)
    if bullet_type==2:
        viata1-=random.randint(5,20)  
    fire=0
    runda=1
    wait=1
############################################################################
#######################################################################VERSIUNE INITIALA
  #fire_bullet(fire,force_enemy,enemy_angle_bullet)
  #fire_bullet(fire,force_enemy,enemy_angle_bullet)
  #button("",150,450,100,50,(10,10,10),(100,10,10),rand_terrain)
#######################################################################
  
  for event in pygame.event.get():
    if event.type is pygame.QUIT:
      running=False
      ##################################################
  if keys[pygame.K_a] and fuel_player>0:
       X_change=-2
       if playX>20:
        fuel_player-=0.5
  if keys[pygame.K_d] and fuel_player>0:
        X_change=2
        if playX<980:
         fuel_player-=0.5
  if playX<20:
      playX=20
  if playX>980:
      playX=980
  playX+=X_change
  playY=height-inaltime[playX]
    ##################################################
  if keys[pygame.K_LEFT] and fuel_enemy>0:
       enX_change=-2
       if enX>20:
        fuel_enemy-=0.5
  if keys[pygame.K_RIGHT] and fuel_enemy>0:
        enX_change=2
        if enX<980:
         fuel_enemy-=0.5
  enX=enX+enX_change
  if enX<20:
      enX=20
  if enX>980:
      enX=980
  enY=height-inaltime[enX]    
##################################################  
  if  life.see(viata1,viata2)==1:
    run=True
    while run:
     win.fill((255,153,51))
     life.winner(viata1,viata2,win)
     pygame.display.update()
     for event in pygame.event.get():
      if event.type is pygame.QUIT:
       run=False
       running=False
  if wait!=0 and life.see(viata1,viata2)==0:
   if runda==1:
     life.arrow(win,playX,playY,wait)
   else:
     life.arrow(win,enX,enY,wait)
   wait+=0.3
   #print(wait)
   if wait>=10:
     wait=0
  pygame.display.update()
pygame.quit()
sys.exit()

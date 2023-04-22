import pygame
import math

img_bullet=pygame.image.load('circle.png')
clock = pygame.time.Clock()
"""
def fire_bullet(height,win,width,bulX,bulY,inaltime,fire):
     if bulY<=height-inaltime[int(bulX)] and bulX>1 and bulX<width-10:
      #clock.tick(100)
      pygame.display.update()
      pygame.draw.circle(win, (0,0,0), (int(bulX), int(bulY)), 2, 2)
      #win.blit(img_bullet,(int(bulX),int(bulY)))
      pygame.display.update()
      return fire
     else:
      return 0
"""

def fire_bullet(playX,playY,force,angle,inaltime,win,height,width,acceleration):
     angle=math.radians(angle)
     bulX=playX
     bulY=playY-5
     factor=force/2
     if acceleration==1:
        prop1=0.5
     if acceleration==2:
        prop1=0.2
     if acceleration==3:
        prop1=1
     if acceleration==4:
        prop1=0.1
     factorX=factor*math.cos(angle)
     factorY=factor*math.sin(angle)
     while   bulX>1 and bulX<width-10 and bulY<=height-inaltime[int(bulX)]:
      clock.tick(25)
      pygame.display.update()
      ####################################PENTRU A PUTEA INCHIDE JOCUL IN TIMP CE ZBOARA PROIECTILUL
      
      for event in pygame.event.get():
       if event.type is pygame.QUIT:
           pygame.quit()
   
      ########################################
      if acceleration!=4:
       pygame.draw.circle(win, (0,0,0), (int(bulX), int(bulY)), 2, 2)
      else:
       pygame.draw.circle(win, (255,255,255), (int(bulX), int(bulY)), 2, 2)
      #win.blit(img_bullet,(int(bulX),int(bulY)))
      bulX+=factorX
      bulY-=factorY
      factorY-=prop1
      pygame.display.update()
     return bulX
def fire_rocket(playX,playY,angle,inaltime,win,height,width,acceleration,enX,enY,player):
     angle=math.radians(angle)
     bulX=playX
     bulY=playY-5
     factor=18
     if acceleration==1:
        prop1=0.8
     if acceleration==2:
        prop1=0.6
     if acceleration==3:
        prop1=1
     if acceleration==4:
        prop1=0.4
     factorX=factor*math.cos(angle)
     factorY=factor*math.sin(angle)
     nr=0
     while  nr<25:
      nr+=1
      clock.tick(40)
      pygame.display.update()
      ####################################PENTRU A PUTEA INCHIDE JOCUL IN TIMP CE ZBOARA PROIECTILUL
      
      for event in pygame.event.get():
          if event.type is pygame.QUIT:
              pygame.quit()
   
      ########################################
     
      pygame.draw.circle(win, (200,10,10), (int(bulX), int(bulY)), 3, 3)
      #win.blit(img_bullet,(int(bulX),int(bulY)))
      bulX+=factorX
      bulY-=factorY
      factorY-=prop1
      pygame.display.update()
     if enX!=bulX:
         fraction=((enY-bulY)/(enX-bulX))
     else:
         fraction=50
     while abs(bulX-enX)>10:
          clock.tick(40)
          if enX-bulX>0:
              bulX+=10
          else:
              bulX-=10
          if enX-bulX>0:
              bulY+=10*fraction
          else:
              bulY-=10*fraction
          pygame.draw.circle(win, (200,10,10), (int(bulX), int(bulY)), 3, 2)
          pygame.display.update()
     return bulX
         
def multiple_fire():
    """
    a
    """
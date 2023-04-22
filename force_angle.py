import pygame
import math

def text_objects(text, font,color):
    textSurface = font.render(text, True, (100,0,100))
    return textSurface, textSurface.get_rect()
  
def traj_angle(angle,win,playX,playY,force_player,position1,position2,runda):
  smallText = pygame.font.SysFont("comicsansms",20)
  angle_rad=(angle*3.1415926)/180
  if runda!=1:
    angle=180-angle
############LINII
  """
  pygame.draw.line(win,(250,245,75),(playX+1,playY-8),(playX+4+force_player*math.cos(-angle_rad),playY+force_player*math.sin(-angle_rad)-10))
  pygame.draw.line(win,(255,255,51),(playX+4,playY-11),(playX+4+force_player*math.cos(-angle_rad),playY+force_player*math.sin(-angle_rad)-10))
  """  
###########Buline
  X=playX+math.cos(-angle_rad)
  Y=playY+math.sin(-angle_rad)-5
  i=1
  if force_player>10:
   force=force_player/30
  else:
   force=0.25
  while i<6:
      pygame.draw.circle(win, (250,245,75), (X, Y), 2, 2)
      X+=force*10*math.cos(-angle_rad)
      Y+=force*10*math.sin(-angle_rad)
      i+=1
#ANGLE DISPLAY  
  textSurf, textRect = text_objects("Unghi: "+str(angle)+"°", smallText,(255,0,127))
  textRect.center = ( position1, position2)
  win.blit(textSurf, textRect)
 #FORCE DISPLAY 
  txtSurf, txtRect = text_objects("Forta: "+str(force_player)+" N", smallText,(186,100,100))
  txtRect.center = ( position1+60, position2-23)
  R=int(2.55*(40-force_player))
  G=force_player*1.5
  B=int(force_player*5)
  if R>255:
     R=255
  if G>255:
     G=255
  if B>255:
    B=255
  color=(R,G,B)
  pygame.draw.rect(win, (0, 0, 0), (position1-52, position2-32, 48, 23), 2)
  pygame.draw.rect(win, color, (position1-50, position2-30, force_player+5, 20))
  win.blit(txtSurf, txtRect)
  

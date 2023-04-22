import math
import pygame

def get_rotation(playX,height,inaltime):
  block_X_front=playX+10
  block_X_back=playX
  block_Y_front=height-inaltime[block_X_front]
  block_Y_back=height-inaltime[block_X_back]
  fraction=(block_Y_front-block_Y_back)/(block_X_front-block_X_back)
  rotation_angle=math.atan(fraction)
  rotation_angle*=180/3.141592
  return rotation_angle

def player(playX,playY,height,inaltime,win,player):
  playerImg = pygame.image.load('tank.png')
  if player==1:
   playerImg= pygame.transform.flip(playerImg, True, False)
  rotation_angle=get_rotation(playX,height,inaltime)
  if player==1:
   playerImg = pygame.transform.rotate(playerImg, (-1)*rotation_angle+18)
  else:
   playerImg = pygame.transform.rotate(playerImg, (-1)*rotation_angle-18)
  win.blit(playerImg, (playX-16, playY-25))
  #Afiseaza punctul coordonatelor X,Y
  #point = pygame.image.load('point.png')
  #win.blit(point, (playX, playY))
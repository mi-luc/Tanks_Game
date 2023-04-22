import random
import pygame

def text_objects(text, font,color):
    textSurface = font.render(text, True, (100,0,100))
    return textSurface, textSurface.get_rect()
  
def display_fuel(win,fuel_level,position1,position2):
  R=int(abs(2.55*(100-fuel_level)))
  G=fuel_level//10
  B=int(fuel_level*2)
  if R>255:
    R=255
  if G>255:
    G=255
  if B>255:
    B=255
  color=(R,G,B)
  smallText = pygame.font.SysFont("comicsansms",20)
  textSurf, textRect = text_objects("Fuel ("+str(fuel_level)+")", smallText,color)
  pygame.draw.rect(win, (0, 0, 0), (position1-2, position2-2, 108, 23), 2) 
  textRect.center = ( position1+170, position2+10 )
  win.blit(textSurf, textRect)
  pygame.draw.rect(win, color, pygame.Rect(position1, position2, fuel_level+5, 20))


def spawnfuel(number,width):
  X_cans=[]
  for i in range(number):
    if i%2==0:
     X_cans.append(random.randint(30,width//2))
    else:
     X_cans.append(random.randint(width//2,width-30))
  return X_cans
    
def show_cans(Xlist,height,inaltime,win):
  img_can=pygame.image.load('jerrycan.png')
  for i in range(len(Xlist)):
   Y=height-inaltime[Xlist[i]]
   win.blit(img_can, (Xlist[i],Y-10))
   
def get_fuel(fuel_player,playX,X_cans):
  for elem in X_cans:
    if elem>=playX-5 and elem<=playX+5:
      return 60
 
  return 0
    
def update_list(fuel_player,playX,X_cans):
  for elem in X_cans:
    if elem>=playX-5 and elem<=playX+5:
      X_cans.remove(elem)
  return X_cans
   
 
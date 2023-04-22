import pygame

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def print_life(life,x,y,win):
    smallText = pygame.font.SysFont("comicsansms",23)
    textSurf, textRect = text_objects("Viata: "+str(life), smallText,(255,160,122))
    textRect.center = ( x, y)
    win.blit(textSurf, textRect)
def see(life1,life2):
   if life1<=0:
      return 1
   if life2<=0:
     return 1
   return 0
def winner(life1,life2,win):
  smallText = pygame.font.SysFont("comicsansms",35)
  if life1<=0:
    textSurf, textRect = text_objects("PLAYER 2 WINS", smallText,(255,51,51))
    j=0
    while j<3:
     i=0
     while i<5:
      textRect.center = (200+j*300,100+i*100)
      win.blit(textSurf, textRect)
      i+=1
     j+=1
    
  if life2<=0:
    textSurf, textRect = text_objects("PLAYER 1 WINS", smallText,(255,51,51))
    j=0
    i=0
    while j<3:
     i=0
     while i<5:
      textRect.center = (200+j*300,100+i*100)
      win.blit(textSurf, textRect)
      i+=1
     j+=1
    
def arrow(win,x,y,i):
  arr=pygame.image.load('arrow.png')
  arr=pygame.transform.rotate(arr,-90)
  win.blit(arr, (x, y-70+i))
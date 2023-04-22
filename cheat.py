import pygame,math

def get_force(win,playX,playY,targetX,targetY,angle,width,inaltime,height,acceleration):
    best=50
    dist=900
    i=1
    angle1=math.radians(angle)
    if acceleration==1:
        prop1=0.5
    if acceleration==2:
        prop1=0.2
    if acceleration==3:
        prop1=1
    if acceleration==4:
        prop1=0.1
    while i<=40:
        bulX=playX
        bulY=playY-5
        factor=i*1.3/2
        factorX=factor*math.cos(angle1)
        factorY=factor*math.sin(angle1)
        while   bulX>1 and bulX<width-10 and bulY<=height-inaltime[int(bulX)]:
            bulX+=factorX
            bulY-=factorY
            factorY-=prop1
        if abs(bulX-targetX)<dist:
          best=i
          dist=abs(bulX-targetX)
        i+=1
    meniu_font=pygame.font.SysFont('bahnschrift',20)
    if dist<50:
     txt1= meniu_font.render("CHEAT: "+str(best)+" dist: "+str(int(dist)),True,(255,0,0))
    else:
     txt1= meniu_font.render("NU E BUN UNGHIUL",True,(0,255,255))
    win.blit(txt1,(400,100))
    """
     X=targetX-playX
     Y=targetY-playY
     print(X,Y,angle)
     prop1=0.5
     angle_rad=math.radians(angle)
     tangent=math.tan(angle_rad)
     if 2*(tangent*X-Y)>=0.001:
      forceX=X*math.sqrt(prop1/(2*(tangent*X-Y)))
      force=forceX/math.cos(angle_rad)*2
     meniu_font=pygame.font.SysFont('bahnschrift',50)
     txt1= meniu_font.render(str(force),True,(0,0,0))
     win.blit(txt1,(200,200))
       """  
from this import d
import src.village as village
from src.inputx import input_to,Get
import sys
import os
from src.spell import sp 
from src.building import build,walls,canon1,canon2,canon3,tower1,tower2
from src.troops import k
import time
from colorama import Fore, Back, Style
from src.troops import * 


rep = []
f=0
time1= time.time()
king_=0
c= input("press K if you want king else press Q")
if c=="k" or c=="K":
    king_=1

while True:
    win =1
    lost = 1
    f= not f
    #display all building
    for b in build:
        if(not b.destroyed):
            win =0
        b.display(b.sizex,b.sizey,b.symbole)
    
    if(win ==1):
        print("Victory")
        break
    
    #king/Queen
    if king_==1:
        k.display()
    else:
        q.display()


    #walls
    for w in  walls:
        w.display(w.sizex,w.sizey,w.symbole)

    
    if(f==1):
        canon1.shoot()
        canon2.shoot()
        canon3.shoot()
        tower1.shoot()
        tower2.shoot()
    #Display village

    village.display_Village()

    canon1.reset_color()
    canon2.reset_color()  
    canon3.reset_color()
    tower1.reset_color()
    tower2.reset_color()

    #display king's health
    if king_:
        k.display_health()
    else:
        q.display_health()

    #barberians
    for barb in barberian.barb_obj:
        if(barb.dead==0):
            lost = 0
            barb.move()
            barb.display(barberian.symbole)
            barb.attack() 

    #Arechers
    for arch in archers.archer_obj:
        print(archers.archer_obj)
        if (len(archers.archer_obj) >5):
            break
        if(arch.dead==0):
            lost = 0
            arch.move()
            arch.display(archers.symbole)
            arch.attack() 
    
    #ballons
    for ballon in ballons.ballon_obj:
        if(ballon.dead==0):
            lost = 0
            ballon.move()
            ballon.display(ballons.symbole)
            ballon.attack() 

    #lost condition
    if(len(barberian.barb_obj)== barberian.max_barberian and lost):
        print("***Defeat****")
        break
    #input
    key = input_to(Get())
    rep.append(time.time()-time1)
    time1 =time.time()
    rep.append(key) 
    if key == 'q':
        break
    spawn(key)
    sp.which_spell(key)
    if (king_):
        if(k.dead==0):
            k.move(key)
            if(key == " "):
                k.attack()
            elif(key == "x"  or key =="X"):
                k.axe_attack()

    else:
        if(q.dead==0):
            q.move(key)
            if(key == " "):
                q.attack()

    os.system('clear')
    
with open('replays/replay.txt', 'w+') as filehandle:
    for listitem in rep:
        filehandle.write('%s\n' % listitem)
#input_to() 
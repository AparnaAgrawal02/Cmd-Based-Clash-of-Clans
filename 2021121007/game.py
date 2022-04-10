from this import d
import src.village as village
from src.inputx import input_to,Get
import sys
import os
from src.spell import sp 
from src.building import build,walls,canon1,canon2,canon3
from src.troops import k
import time
from colorama import Fore, Back, Style
from src.troops import * 


rep = []
f=0
time1= time.time()

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
    
    #king
    k.display()
    #walls
    for w in  walls:
        w.display(w.sizex,w.sizey,w.symbole)

    #display king's health
    if(f==1):
        canon1.shoot()
        canon2.shoot()
        canon3.shoot()
    #Display village

    village.display_Village()
    canon1.reset_color() 
    canon2.reset_color()  
    canon3.reset_color() 
    k.display_health()

    #barberians
    for barb in barb_obj:
        barb.display()
        if(barb.dead==0):
            lost = 0
            barb.move()
            barb.attack() 
    #lost condition
    if(len(barb_obj)== max_barberian and lost):
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
    if 
    if(k.dead==0):
        k.move(key)
        if(key == " "):
            k.attack()
        elif(key == "x"  or key =="X"):
            k.axe_attack()
    os.system('clear')
    
with open('replays/replay.txt', 'w+') as filehandle:
    for listitem in rep:
        filehandle.write('%s\n' % listitem)
#input_to() 
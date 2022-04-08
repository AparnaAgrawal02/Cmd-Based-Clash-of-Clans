from this import d
from src.village import *
import sys
import os
from src.spell import sp 
from src.building import *
from src.troops import k
import time
from colorama import Fore, Back, Style
from src.troops import * 
# define an empty list

def replay():
    rep= []
    f=0
    pos=-1
    # open file and read the content in a list
    with open('replays/replay.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentcmd = line[:-1]

            # add item to the list
            rep.append(currentcmd)
    while True:
        pos+=1
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

        display_Village()
        canon1.reset_color() 
        canon2.reset_color()  
        canon3.reset_color() 
        k.display_health()

        #barberians
        for barb in barb_obj:
            if(barb.dead==0):
                lost = 0
                barb.move()
                barb.display()
                barb.attack() 
        #lost condition
        if(len(barb_obj)== max_barberian and lost):
            print("***Defeat****")
            break
        #input
        time.sleep(float(rep[pos]))
        pos+=1
        key = rep[pos]
        if key == 'q':
            break
        spawn(key)
        sp.which_spell(key)
        if(k.dead==0):
            k.move(key)
            if(key == " "):
                k.attack()
            elif(key == "x"  or key =="X"):
                k.axe_attack()
        os.system('clear')
replay()
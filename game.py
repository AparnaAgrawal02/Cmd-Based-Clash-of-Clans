from this import d
import src.village as village
from src.inputx import input_to,Get
import sys
import os
from src.spell import sp 
from src.building import reset_build,build,defence_build, level,walls,canon1,canon2,canon3,tower1,tower2,canon4,tower3, tower4
from src.troops import k
import time
from colorama import Fore, Back, Style
from src.troops import * 


rep = []
f=0
time1= time.time()
king_=0
lev = 1
[defence_build,build] = level(lev,build)
c= input("press K if you want king else press Q")
if c=="k" or c=="K":
    king_=1
defeat = False
Eattack =0
while lev !=4:
    if(defeat):
        break
    while True:
        print("LEVEL:"+str(lev))
        win =1
        lost = 1
        f= not f
        #display all building
        for b in build:
            if(not b.destroyed):
                win =0
            #print(b.symbole)
            b.display(b.sizex,b.sizey,b.symbole)
        
        if(win ==1 and lev !=3):
            win=0
            lev+=1
            print("HURRAY PROCCEDED TO LEVEL:"+str(lev))
            reset_build()
            [village.village_object,village.village] =village.reset_village()
            reset_troops()
            break
        elif(win==1):
            print("VICTORY!!!!")
            lev+=1
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
            for db in defence_build:
                db.shoot()
        #Display village

        #barberians
        for barb in barberian.barb_obj:
            if(barb.dead==0):
                lost = 0
                barb.move()
                barb.attack() 
            barb.display(barberian.symbole)

        #Arechers
        for arch in archers.archer_obj:
            #print(archers.archer_obj)
            if(arch.dead==0):
                lost = 0
                arch.move()
                arch.attack() 
            arch.display(archers.symbole)
        
        #ballons
        for ballon in ballons.ballon_obj:
            if(ballon.dead==0):
                lost = 0
                ballon.move()
                ballon.attack()
            ballon.display(ballons.symbole) 

        village.display_Village()

        for db in defence_build:
                db.shoot()

        #display king's health
        if king_:
            k.display_health()
        else:
            q.display_health()

        

        #lost condition
        if(len(barberian.barb_obj)== barberian.max_barberian and len(archers.archer_obj)== archers.max_archers and len(ballons.ballon_obj)== ballons.max_ballons and lost):
            print("***Defeat****")
            defeat =True
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
            Etime =0
            if(q.dead==0):
                q.move(key)
                if(key == " "):
                    q.attack()
                elif(key == "x"  or key =="X"):
                    Eattack = 1
                    Etime =  time.time()

                
            if(Eattack and  time.time() - Etime > 1):
                q.Eagle_attack()


        os.system('clear')
    
with open('replays/replay.txt', 'w+') as filehandle:
    for listitem in rep:
        filehandle.write('%s\n' % listitem)
#input_to() 
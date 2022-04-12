

from dataclasses import replace
from operator import truediv
from re import I
import src.village as village

import src.building as building
from sys import stdout
from colorama import Fore
from colorama import init as colorama_init
import math

#SPAWNNING POINT
s1 =[0,village.n-1]
s2 =[village.n-1,0]
s3= [village.n-1,village.m-1]
class troop():

    def __init__(self,health,speed=1,i=0,j=0):
        self.health = health
        self.current_health = self.health
        self.i=i
        self.j=j
        self.dead =0
        self.step = speed
        self.replaced = Fore.LIGHTWHITE_EX  + "\u2592" 
        self.replaced_obj =  Fore.LIGHTWHITE_EX  + "\u2592" 
        

    def check_boundry(self,x,y):
        if(x<village.n and y<village.m and x>=0 and y>=0 ):
            return True
        else: 
            return False

    def attack(self):

        #print(village.village_object[self.i][self.j+1],village.village_object[self.i][self.j+1])
        if(self.check_boundry(self.i,self.j+1)):
            obj =village.village_object[self.i][self.j+1]
            represent  = village.village[self.i][self.j+1]
        if(self.check_boundry(self.i,self.j-1)):   
            obj1 = village.village_object[self.i][self.j-1]
            represent1  = village.village[self.i][self.j-1]
        if(self.check_boundry(self.i+1,self.j)):
            obj2 = village.village_object[self.i+1][self.j]
            represent2  = village.village[self.i+1][self.j]
        if(self.check_boundry(self.i-1,self.j)):
            obj3 = village.village_object[self.i-1][self.j]
            represent3  = village.village[self.i-1][self.j]
        if(self.check_boundry(self.i,self.j+1) and obj != Fore.LIGHTWHITE_EX  + "\u2592" and represent[-1]!='B'and represent[-1]!='K' and represent[-1]!='A' and represent[-1]!="\u03A6" and represent[-1]!='Q' ):
            #print(village.village_object[self.i][self.j+1].symbole)
            obj.current_health-=self.damage
            #print(village.village_object[self.i][self.j+1],village.village_object[self.i][self.j+1].health)

        elif(self.check_boundry(self.i,self.j-1) and obj1 != Fore.LIGHTWHITE_EX  + "\u2592" and represent1[-1]!='B'and represent1[-1]!='K' and represent[-1]!='A' and represent[-1]!="\u03A6" and represent[-1]!='Q' ):
            #print(village.village_object[self.i][self.j-1].symbole)
            obj1.current_health-=self.damage
        elif(self.check_boundry(self.i+1,self.j) and obj2 != Fore.LIGHTWHITE_EX  + "\u2592" and represent2[-1]!='B'and represent2[-1]!='K' and represent[-1]!='A' and represent[-1]!="\u03A6" and represent[-1]!='Q' ):
            obj2.current_health-=self.damage
            #print(village.village_object[self.i+1][self.j].symbole)
        elif(self.check_boundry(self.i-1,self.j) and obj3 != Fore.LIGHTWHITE_EX  + "\u2592" and represent3[-1]!='B'and represent3 [-1]!='K'and represent[-1]!='A'and represent[-1]!="\u03A6" and represent[-1]!='Q'):
            obj3.current_health-=self.damage
            #print(village.village_object[self.i-1][self.j].symbole)

    def display(self,symbole):
        if(self.current_health>25 and self.current_health<40):
            self.color = Fore.LIGHTBLACK_EX
        elif(self.current_health<25 and self.current_health>10):
            self.color = Fore.BLUE
        elif(self.current_health<10):
            self.color = Fore.WHITE
        village.village[self.i][self.j]= self.color+symbole
        village.village_object[self.i][self.j] =self

    def move(self):
        if not self.dead:
            village.village[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592" 
            village.village_object[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592" 
            self.change_position()
            village.village_object[self.i][self.j] = self
    
   
            
    
class king(troop):
    damage = 10
    axe_range = 5
    def display(self):
        village.village[self.i][self.j]=Fore.MAGENTA+"K"
        village.village_object[self.i][self.j] =self

    def change_position(self,key):
        for _ in range(0,self.step):
            if((key == 'W' or key =='w' )and  self.check_boundry(self.i-1,self.j) and village.village[self.i-1][self.j] == Fore.LIGHTWHITE_EX  + "\u2592"):
                    self.i-=1
            elif((key == 'A' or key == 'a') and  self.check_boundry(self.i,self.j-1) and village.village[self.i][self.j-1] == Fore.LIGHTWHITE_EX  + "\u2592"):
                    self.j-=1
            
            elif((key == 'S' or key == 's' )and  self.check_boundry(self.i+1,self.j) and village.village[self.i][self.j] == Fore.LIGHTWHITE_EX  + "\u2592"):
                    self.i+=1
            elif((key == 'D' or key =='d') and  self.check_boundry(self.i,self.j+1) and village.village[self.i][self.j+1] == Fore.LIGHTWHITE_EX  + "\u2592"):
                    self.j+=1
    
    def move(self,key):
        village.village[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592"
        
        village.village_object[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592" 
        self.change_position(key)
        village.village_object[self.i][self.j] = self
    
        village.village[self.i][self.j] = Fore.MAGENTA+"K"

    def attack(self):
        #print(village.village_object[self.i][self.j+1],village.village_object[self.i][self.j+1])
        if(self.check_boundry(self.i,self.j+1) and village.village_object[self.i][self.j+1] != Fore.LIGHTWHITE_EX  + "\u2592"):
            village.village_object[self.i][self.j+1].current_health-=self.damage
            #print(village.village_object[self.i][self.j+1],village.village_object[self.i][self.j+1].health)

    def axe_attack(self):
        reduce = set()
        for i in range(self.i-self.axe_range,self.i+self.axe_range+1):
            if(i>=village.n or i<0 ):
                continue
            for j in range(self.j-self.axe_range,self.j+self.axe_range+1):
                if(j>=village.m or j<0 or (self.i == i and self.j == j )):
                    continue
                if village.village_object[i][j] in building.build and not village.village_object[i][j].destroyed :
                    reduce.add(village.village_object[i][j])
            
        for x in reduce:
            x.current_health-=self.damage
                    


    def display_health(self):
        print("king:",end ="")
        for _ in range(int(20*(self.current_health/self.health))):
            print("*",end="")
        print(" ")

class archerQueen(troop):
    damage = 10
    axe_range = 5
    pos_of_EA_ix=0
    pos_of_EA_iy=0
    pos_of_EA_jx=0
    pos_of_EA_jy=0

    last_moved_direc=[0,1]
    def display(self):
        village.village[self.i][self.j]=Fore.MAGENTA+"Q"
        village.village_object[self.i][self.j] =self

    def change_position(self,key):
        for _ in range(0,self.step):
            if((key == 'W' or key =='w' )and  self.check_boundry(self.i-1,self.j) and village.village[self.i-1][self.j] == Fore.LIGHTWHITE_EX  + "\u2592"):
                    self.i-=1
                    archerQueen.last_moved_direc=[-1,0]
                    
            elif((key == 'A' or key == 'a') and  self.check_boundry(self.i,self.j-1) and village.village[self.i][self.j-1] == Fore.LIGHTWHITE_EX  + "\u2592"):
                    self.j-=1
                    archerQueen.last_moved_direc=[0,-1]
            
            elif((key == 'S' or key == 's' )and  self.check_boundry(self.i+1,self.j) and village.village[self.i][self.j] == Fore.LIGHTWHITE_EX  + "\u2592"):
                    self.i+=1
                    archerQueen.last_moved_direc=[1,0]
            elif((key == 'D' or key =='d') and  self.check_boundry(self.i,self.j+1) and village.village[self.i][self.j+1] == Fore.LIGHTWHITE_EX  + "\u2592"):
                    self.j+=1
                    archerQueen.last_moved_direc=[0,1]

    
    def move(self,key):
        village.village[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592"
        
        village.village_object[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592" 
        self.change_position(key)
        village.village_object[self.i][self.j] = self
    
        village.village[self.i][self.j] = Fore.MAGENTA+"Q"

    def attack(self):
        arr= set()
        for i in range(self.i-2+archerQueen.last_moved_direc[0]*8,self.i+2+1+archerQueen.last_moved_direc[0]*8):
            for j in range(self.j-2+archerQueen.last_moved_direc[1]*8,self.j+2+1+archerQueen.last_moved_direc[1]*8):
                if(self.check_boundry(i,j)):
                    obj =village.village_object[i][j]
                    represent  = village.village[i][j]

                if(self.check_boundry(i,j) and obj != Fore.LIGHTWHITE_EX  + "\u2592" and represent[-1]!='B'and represent[-1]!='K' and represent[-1]!='A' and represent[-1]!="\u03A6"):
                    #print(village.village_object[self.i][self.j+1].symbole)
                    arr.add(obj)
            
        for x in arr:
            x.current_health-=self.damage

    def setForEAttack(self):
        self.pos_of_EA_ix=self.i-4+archerQueen.last_moved_direc[0]*16
        self.pos_of_EA_iy=self.i+4+1+archerQueen.last_moved_direc[0]*16
        self.pos_of_EA_jx=self.j-4+archerQueen.last_moved_direc[1]*16
        self.pos_of_EA_jy=self.j+4+1+archerQueen.last_moved_direc[1]*16
    
    def Eagle_attack(self):
        arr= set()
        for i in range(self.pos_of_EA_ix,self.pos_of_EA_iy):
            for j in range(self.pos_of_EA_jx,self.pos_of_EA_jy):
                if(self.check_boundry(i,j)):
                    obj =village.village_object[i][j]
                    represent  = village.village[i][j]

                if(self.check_boundry(i,j) and obj != Fore.LIGHTWHITE_EX  + "\u2592" and represent[-1]!='B'and represent[-1]!='K' and represent[-1]!='A' and represent[-1]!="\u03A6"):
                    #print(village.village_object[self.i][self.j+1].symbole)
                    arr.add(obj)
            
        for x in arr:
            x.current_health-=self.damage


    

    def display_health(self):
        print("Queen:",end ="")
        for _ in range(int(20*(self.current_health/self.health))):
            print("*",end="")
        print(" ")

class barberian(troop):
    damage = 5
    color = Fore.BLACK
    barb_obj=[]
    speed = 1
    max_barberian = 6
    heal=50
    symbole = "B"
    


    def change_position(self):
        for _ in range(0,self.step):
            min1=village.n*village.m 
            cord = []
            for b in building.build:
                if not b.destroyed:
                    dist = math.sqrt((b.x+b.center[0]-self.i)**2 + (b.y+b.center[1]-self.j)**2)
                    if(dist<min1):
                        min1 =dist
                        cord =[b.x+b.center[0],b.y+b.center[1]]
            if cord ==[]:
                return
            if(cord[0]>self.i and (village.village[self.i+1][self.j]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]==barberian.symbole or village.village[self.i+1][self.j][-1]=='K'or village.village[self.i+1][self.j][-1]==archers.symbole or village.village[self.i+1][self.j][-1]==ballons.symbole)):
                self.i+=1
            if(cord[0]<self.i and (village.village[self.i-1][self.j]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]==barberian.symbole or village.village[self.i+1][self.j][-1]=='K' or village.village[self.i+1][self.j][-1]==archers.symbole or village.village[self.i+1][self.j][-1]==ballons.symbole)):
                self.i-=1
            if(cord[1]>self.j and (village.village[self.i][self.j+1]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]==barberian.symbole or village.village[self.i+1][self.j][-1]=='K'or village.village[self.i+1][self.j][-1]==archers.symbole or village.village[self.i+1][self.j][-1]==ballons.symbole )):
                self.j+=1
            if(cord[1]<self.j and (village.village[self.i][self.j-1]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]==barberian.symbole or village.village[self.i+1][self.j][-1]=='K' or village.village[self.i+1][self.j][-1]==archers.symbole or village.village[self.i+1][self.j][-1]==ballons.symbole)):
                self.j-=1
        
    
class archers(troop):   
    damage = barberian.damage/2
    heal = barberian.heal/2
    speed = barberian.speed*2
    color = Fore.BLACK
    archer_obj=[]
    damage_range = 6 
    max_archers = 6 
    symbole = "A"

    def change_position(self):
        for _ in range(0,self.step):
            min1=village.n*village.m 
            cord = []
            for b in building.build:
                if not b.destroyed:
                    dist = math.sqrt((b.x+b.center[0]-self.i)**2 + (b.y+b.center[1]-self.j)**2)
                    if(dist<min1):
                        min1 =dist
                        cord =[b.x+b.center[0],b.y+b.center[1]]
        
            if cord ==[]:
                return
            if (min1 < archers.damage_range):
                #print("WHHHHATT")
                return

            if(cord[0]>self.i and (village.village[self.i+1][self.j]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K' or village.village[self.i+1][self.j][-1]=='Q'or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K' or village.village[self.i+1][self.j][-1]=='A')):
                self.i+=1
            if(cord[0]<self.i and (village.village[self.i-1][self.j]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K'or village.village[self.i+1][self.j][-1]=='Q') or village.village[self.i+1][self.j][-1]=='A'):
                self.i-=1
            if(cord[1]>self.j and (village.village[self.i][self.j+1]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K'  or village.village[self.i+1][self.j][-1]=='Q') or village.village[self.i+1][self.j][-1]=='A'):
                self.j+=1
            if(cord[1]<self.j and (village.village[self.i][self.j-1]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K' or village.village[self.i+1][self.j][-1]=='Q') or village.village[self.i+1][self.j][-1]=='A'):
                self.j-=1
    
    def attack(self):
        if self.dead:
            return
        
        cord =[]
        min1=village.n*village.m 
        for b in building.build:
            if not b.destroyed:
                dist = math.sqrt((b.x+b.center[0]-self.i)**2 + (b.y+b.center[1]-self.j)**2)
                if(dist<min1):
                    min1 =dist
                    cord =[b.x+b.center[0],b.y+b.center[1]]
                    closer_build=b
        
        if cord ==[]:
            return
        if (min1 < archers.damage_range):
            #print("FFFFFFFFFFFFFFIN")
            closer_build.current_health-=self.damage

    

        



class ballons(troop):   
    damage = 2*barberian.damage
    heal = barberian.heal
    speed = barberian.speed*2
    color = Fore.BLACK
    ballon_obj=[]
    damage_range = 9 
    max_ballons= 3
    symbole = "\u03A6"

    def change_position(self):
        for _ in range(0,self.step):
            min1=village.n*village.m 
            cord = []

            for b in building.defence_build:
                if not b.destroyed:
                    dist = math.sqrt((b.x+b.center[0]-self.i)**2 + (b.y+b.center[1]-self.j)**2)
                    if(dist<min1):
                        min1 =dist
                        cord =[b.x+b.center[0],b.y+b.center[1]]

            if cord ==[]:
                for b in building.build:
                    if not b.destroyed:
                        dist = math.sqrt((b.x+b.center[0]-self.i)**2 + (b.y+b.center[1]-self.j)**2)
                        if(dist<min1):
                            min1 =dist
                            cord =[b.x+b.center[0],b.y+b.center[1]]
                 
        
            if cord ==[]:
                return

            
            if(cord[0]>self.i):
                self.i+=1
            if(cord[0]<self.i):
                self.i-=1
            if(cord[1]>self.j ):
                self.j+=1
            if(cord[1]<self.j ):
                self.j-=1

    def attack(self):
        if self.dead:
            return
        for _ in range(0,self.step):
            min1=village.n*village.m 
            cord = []

            # instead of making two list could have goven weights to defece_buildings higher than normal and comepare that too...!
            for b in building.defence_build:
                if not b.destroyed:
                    dist = math.sqrt((b.x+b.center[0]-self.i)**2 + (b.y+b.center[1]-self.j)**2)
                    if(dist<min1):
                        min1 =dist
                        cord =[b.x+b.center[0],b.y+b.center[1]]
                        closer_build=b

            if cord ==[]:
                for b in building.build:
                    if not b.destroyed:
                        dist = math.sqrt((b.x+b.center[0]-self.i)**2 + (b.y+b.center[1]-self.j)**2)
                        if(dist<min1):
                            min1 =dist
                            cord =[b.x+b.center[0],b.y+b.center[1]]
                            closer_build=b

            if cord ==[]:
                return
            elif(cord[0]==self.i and cord[1]==self.j):
                closer_build.current_health-=self.damage

    def move(self):
        if not self.dead:
            if((self.replaced_obj in building.build and not self.replaced_obj.destroyed )or (self.replaced[5:] in ['A','Q','K','B',ballons.symbole]  and  self.replaced_obj.dead) ):
                village.village[self.i][self.j] = self.replaced
                village.village_object[self.i][self.j] = self.replaced_obj
            else:
                village.village[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592" 
                village.village_object[self.i][self.j] =  Fore.LIGHTWHITE_EX  + "\u2592" 
            
            self.change_position()
            temp1=village.village[self.i][self.j]
            temp2 = village.village_object[self.i][self.j]
            village.village_object[self.i][self.j] = self
            village.village[self.i][self.j] = self.symbole
            self.replaced = temp1
            self.replaced_obj = temp2



def spawn(key):
    if (key == "0" and len( barberian.barb_obj)<= barberian.max_barberian):
        b= barberian(health =barberian.heal,speed= barberian.speed,i=s1[0],j=s1[1])
        b.display(barberian.symbole)
        barberian.barb_obj.append(b)
    elif(key == "1" and len( barberian.barb_obj)<= barberian.max_barberian):
        b =barberian(barberian.heal,speed= barberian.speed,i=s2[0],j=s2[1])
        b.display(barberian.symbole)
        barberian.barb_obj.append(b)
    elif(key == "2" and len( barberian.barb_obj)<= barberian.max_barberian):
       b=barberian(barberian.heal,speed= barberian.speed,i= s3[0],j=s3[1])
       b.display(barberian.symbole)
       barberian.barb_obj.append(b)

    elif (key == "3" and len( archers.archer_obj)<= archers.max_archers):
        a= archers(health =archers.heal,speed= archers.speed,i=s1[0],j=s1[1])
        a.display(archers.symbole)
        archers.archer_obj.append(a)
        archers.archer_obj
    elif(key == "4" and len(archers.archer_obj)<= archers.max_archers):
        a =archers(archers.heal,speed= archers.speed,i=s2[0],j=s2[1])
        a.display(archers.symbole)
        archers.archer_obj.append(a)
    elif(key == "5" and len( archers.archer_obj)<= archers.max_archers):
       a=archers(archers.heal,speed= archers.speed,i= s3[0],j=s3[1])
       a.display(archers.symbole)
       archers.archer_obj.append(a)
    
    elif (key == "6" and len( ballons.ballon_obj)<= ballons.max_ballons):
        a= ballons(health =ballons.heal,speed= ballons.speed,i=s1[0],j=s1[1])
        a.display(ballons.symbole)
        ballons.ballon_obj.append(a)
    elif(key == "7" and len(ballons.ballon_obj)<= ballons.max_ballons):
        a =ballons(ballons.heal,speed= ballons.speed,i=s2[0],j=s2[1])
        a.display(ballons.symbole)
        ballons.ballon_obj.append(a)
    elif(key == "8" and len( ballons.ballon_obj)<= ballons.max_ballons):
       a=ballons(ballons.heal,speed= ballons.speed,i= s3[0],j=s3[1])
       a.display(ballons.symbole)
       ballons.ballon_obj.append(a)
k = king(100) 
q = archerQueen(100)

def Update_build(build,defence_build):
    [building.build,building.defence_build] = [build,defence_build]
def reset_troops():
    k.current_health = k.health
    q.current_health = q.health
    q.i =0
    q.j=0
    q.step =1
    k.step =1
    k.i=1
    k.j=1
    k.dead=0
    q.dead=0
    ballons.ballon_obj =[]
    archers.archer_obj =[]
    barberian.barb_obj =[]
    



    



 


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
    def __init__(self,health,i=0,j=0):
        self.health = health
        self.current_health = self.health
        self.i=i
        self.j=j
        self.dead =0
        self.step =1
        

    def check_boundry(self,x,y):
        if(x<village.n and y<village.m and x>=0 and y>=0 ):
            return True
        else:
        
            return False

    def attack(self):

        #print(village.village_object[self.i][self.j+1],village.village_object[self.i][self.j+1])
        obj =village.village_object[self.i][self.j+1]
        represent  = village.village[self.i][self.j+1]
        obj1 = village.village_object[self.i][self.j-1]
        represent1  = village.village[self.i][self.j-1]
        obj2 = village.village_object[self.i+1][self.j]
        represent2  = village.village[self.i+1][self.j]
        obj3 = village.village_object[self.i-1][self.j]
        represent3  = village.village[self.i-1][self.j]
        if(self.check_boundry(self.i,self.j+1) and obj != Fore.LIGHTWHITE_EX  + "\u2592" and represent[-1]!='B'and represent[-1]!='K'):
            #print(village.village_object[self.i][self.j+1].symbole)
            obj.current_health-=self.damage
            #print(village.village_object[self.i][self.j+1],village.village_object[self.i][self.j+1].health)

        elif(self.check_boundry(self.i,self.j-1) and obj1 != Fore.LIGHTWHITE_EX  + "\u2592" and represent1[-1]!='B'and represent1[-1]!='K'):
            #print(village.village_object[self.i][self.j-1].symbole)
            obj1.current_health-=self.damage
        elif(self.check_boundry(self.i+1,self.j) and obj2 != Fore.LIGHTWHITE_EX  + "\u2592" and represent2[-1]!='B'and represent2[-1]!='K'):
            obj2.current_health-=self.damage
            #print(village.village_object[self.i+1][self.j].symbole)
        elif(self.check_boundry(self.i-1,self.j) and obj3 != Fore.LIGHTWHITE_EX  + "\u2592" and represent3[-1]!='B'and represent3 [-1]!='K'):
            obj3.current_health-=self.damage
            #print(village.village_object[self.i-1][self.j].symbole)
    
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


class barberian(troop):
    damage = 5
    color = Fore.BLACK
    def display(self):
        if(self.current_health>25 and self.current_health<40):
            self.color = Fore.LIGHTBLACK_EX
        elif(self.current_health<25 and self.current_health>10):
            self.color = Fore.BLUE
        elif(self.current_health<10):
            self.color = Fore.WHITE
        village.village[self.i][self.j]= self.color+"B"
        village.village_object[self.i][self.j] =self

    def move(self):
        if not self.dead:
            village.village[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592" 
            village.village_object[self.i][self.j] = Fore.LIGHTWHITE_EX  + "\u2592" 
            self.change_position()
            village.village_object[self.i][self.j] = self


    def change_position(self):
        for _ in range(0,self.step):
            min1=village.n*village.m 
            cord = []
            for b in building.build:
                if not b.destroyed:
                    dist = math.sqrt((b.x+b.center[0]-self.i)**2 + (b.y+b.center[1]-self.i)**2)
                    if(dist<min1):
                        min1 =dist
                        cord =[b.x+b.center[0],b.y+b.center[1]]
            if cord ==[]:
                return
            if(cord[0]>self.i and (village.village[self.i+1][self.j]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K')):
                self.i+=1
            if(cord[0]<self.i and (village.village[self.i-1][self.j]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K')):
                self.i-=1
            if(cord[1]>self.j and (village.village[self.i][self.j+1]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K')):
                self.j+=1
            if(cord[1]<self.j and (village.village[self.i][self.j-1]== Fore.LIGHTWHITE_EX  + "\u2592" or village.village[self.i+1][self.j][-1]=='B' or village.village[self.i+1][self.j][-1]=='K')):
                self.j-=1
        
    
                

barb_obj=[]
max_barberian = 7

def spawn(key):
    if (key == "0" and len(barb_obj)<=max_barberian):
        b= barberian(health =50,i=s1[0],j=s1[1])
        b.display()
        barb_obj.append(b)
    elif(key == "1" and len(barb_obj)<=max_barberian):
        b =barberian(50,i=s2[0],j=s2[1])
        b.display()
        barb_obj.append(b)
    elif(key == "2" and len(barb_obj)<=max_barberian):
       b=barberian(50,s3[0],s3[1])
       b.display()
       barb_obj.append(b)
k = king(100) 



 
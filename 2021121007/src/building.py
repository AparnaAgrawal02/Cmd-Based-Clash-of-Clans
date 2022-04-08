from ast import For
from re import X
import src.village as village
from sys import stdout
from colorama import Fore, Back, Style
from colorama import init as colorama_init

class Building(object):
    def __init__(self, x,y, health):
            self.x = x
            self.y = y
            self.health = health
            self.destroyed =0
            self.color = Fore.GREEN
            #self.position = position
            self.current_health = health

    def delete_building(self,sizex,sizey):
        self.destroyed =1 
        for i in range(self.x,self.x+sizex):
            for j in range(self.y,self.y+sizey):
                village.village[i][j] =Fore.LIGHTWHITE_EX  + "\u2592"
                village.village_object[i][j]=Fore.LIGHTWHITE_EX  + "\u2592"

    def display(self,sizex,sizey,symbole):
        #print(self.current_health,symbole)
        if self.destroyed==1:
            return 
        #print(self.health,self.current_health) 
        if(self.health*1/2>self.current_health and self.current_health > self.health*1/5): 
        
            self.change_color(Fore.YELLOW,sizex,sizey, symbole)

        elif (self.current_health <self.health*1/5 and  self.current_health>0):
                self.change_color(Fore.RED,sizex,sizey,symbole)
    
        elif (self.current_health<=0):
            self.destroyed=1
            self.delete_building(sizex,sizey)

        elif(self.current_health == self.health):           
            for i in range(self.x,self.x+sizex):
                for j in range(self.y,self.y+sizey):
                    village.village[i][j]=Fore.GREEN + symbole
                    village.village_object[i][j] = self


    
    def reduce_health(self,hit):
        self.current_health -=hit

    def change_color(self,color,sizex,sizey, symbole):
        self.color = color
        for i in range(self.x,self.x+sizex):
            for j in range(self.y,self.y+sizey):
                village.village[i][j] = color +  symbole

       

    
    

class Hut(Building):
    sizex = 2
    sizey = 2 
    symbole = "\u25B2"
    center = [0,0]
    
class Townhall(Building):
    sizex = 3
    sizey = 4 
    symbole = "\u25AC"
    center = [1,2]
class wall(Building):
    sizex = 1
    sizey = 1
    symbole = "\u00D6"
class canon(Building):
    sizex = 3
    sizey = 3
    symbole ="\u25BA"
    range1 = 7
    damage = 5
    center=[1,1]
    def shoot(self):
        if self.destroyed:
            return
        x1=self.x+1
        y1=self.y+1
        shooted =0
        for i in range(x1-self.range1,x1+self.range1+1):
            if(i>=village.n or i<0 ):
                continue
            for j in range(y1-self.range1,y1+self.range1+1):
                if(j>=village.m or j<0 and village.village_object[i][j] == self.color+self.symbole):
                    continue
                if(village.village[i][j][-1]=='K' or village.village[i][j][-1]=="B"):
                    if((not village.village_object[i][j].dead) and village.village_object[i][j].current_health>self.damage):

                           
                        #change canon color
                        for r1 in range(self.x,self.x+self.sizex):
                            for r2 in range(self.y,self.y+self.sizey):
                                village.village[r1][r2] = Fore.CYAN +  self.symbole

                        village.village_object[i][j].current_health-= self.damage
                    else:
                        village.village_object[i][j].current_health=0
                        village.village_object[i][j].dead=1
                    shooted =1  
                    break
            if(shooted):
                break

        
    def reset_color(self):
        if self.destroyed:
            return
        for i in range(self.x,self.x+self.sizex):
            for j in range(self.y,self.y+self.sizey):
                village.village[i][j] = self.color +  self.symbole



townHall = Townhall((village.n-3)//2,(village.m-4)//2,50)
canon1 = canon((village.n)//2,(village.m)//4,30)
canon2 = canon(village.n//4,(village.m)//2,30)
canon3 = canon(3*village.n//4,(village.m)//2,30)
hut1 =  Hut(village.n//4,village.m//4,40)
hut2 =  Hut(3*village.n//4,village.m//4,40)
hut3 =  Hut(village.n//4,3*village.m//4,40)
hut4 =  Hut(3*village.n//4,3*village.m//4,40)
hut5 =  Hut(village.n//2,3*village.m//4,40)

build = [townHall,canon1,canon2,canon3,hut1,hut2,hut3,hut4,hut5]


#wallls
walls = []
i = (village.n-3)//2-2
for j in range((village.m-4)//2-4,(village.m-4)//2+8):
    
    village.village_object[i][j] = wall(i,j,20)
    walls.append(village.village_object[i][j])

i = (village.n-3)//2+4
for j in range((village.m-4)//2-4,(village.m-4)//2+8):
    village.village_object[i][j] = wall(i,j,20)
    walls.append(village.village_object[i][j])

j = (village.m-4)//2-4
for i in range((village.n-3)//2-2,(village.n-3)//2+5):
    village.village_object[i][j] = wall(i,j,20)
    walls.append(village.village_object[i][j])

j = (village.m-4)//2+7
for i in range((village.n-3)//2-2,(village.n-3)//2+5):
    village.village_object[i][j] = wall(i,j,20)
    walls.append(village.village_object[i][j])





#village.display_Village() 
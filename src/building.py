from ast import For
from re import X
import src.village as village
from sys import stdout
from colorama import Fore, Back, Style
from colorama import init as colorama_init
global build,defence_build, level,walls,canon1,canon2,canon3,tower1,tower2,canon4,tower3, tower4

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

    def reset_color(self):
        if self.destroyed:
            return
        for i in range(self.x,self.x+self.sizex):
            for j in range(self.y,self.y+self.sizey):
                village.village[i][j] = self.color +  self.symbole
        

    
    

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
                if(village.village[i][j][-1]=='K' or village.village[i][j][-1]=="B" or village.village[i][j][-1]=="A" or village.village[i][j][-1]=="Q" or village.village[i][j][5:]=="\u03A6"):
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

        
   
        

class wizard_Tower(Building):
    sizex = 3
    sizey = 3
    symbole ="\u2388"
    range1 = 7
    damage = 1
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
                if(village.village[i][j][-1]=='K' or village.village[i][j][-1]=="B" or village.village[i][j][-1]=="A" or village.village[i][j][-1]=="Q" or village.village[i][j][5:]=="\u03A6"):
                    if((not village.village_object[i][j].dead) and village.village_object[i][j].current_health>self.damage):
                        #change wizard color
                        for r1 in range(self.x,self.x+self.sizex):
                            for r2 in range(self.y,self.y+self.sizey):
                                village.village[r1][r2] = Fore.CYAN +  self.symbole

                        village.village_object[i][j].current_health-= self.damage
                    else:
                        village.village_object[i][j].current_health=0
                        village.village_object[i][j].dead=1
                    shooted =1 
                    #print("WHEEEEEEEEE",i,j)
                    #check in 3X3 grid due to AOE
                    for g in range(i-1,i+2):
                        for h in range(j-1,j+2):
                            if(h>=village.m or h<0 and village.village_object[g][h] == self.color+self.symbole):
                                continue
                            if(village.village[g][h][-1]=='K' or village.village[g][h][-1]=="B" or village.village[g][h][-1]=="A" or village.village[g][h][-1]=="Q" or village.village[g][h][5:]=="\u03A6"):
                                if((not village.village_object[g][h].dead) and village.village_object[g][h].current_health>self.damage):

                                    village.village_object[g][h].current_health-= self.damage
                                else:
                                    village.village_object[g][h].current_health=0
                                    village.village_object[g][h].dead=1
                                


                    break
            if(shooted):
                break

  
townHall = Townhall((village.n-3)//2,(village.m-4)//2,50)
canon1 = canon((village.n)//2,(village.m)//4,30)
canon2 = canon(village.n//4,(village.m)//2,30)
canon3 = canon(3*village.n//4,(village.m)//2,30)
canon4 = canon(3*village.n//5,(village.m)//2,30)
tower1 = wizard_Tower(2*village.n//5,2*(village.m)//3,30)
tower2 = wizard_Tower(2*village.n//3,(village.m)//3,30)
tower3 = wizard_Tower(village.n//5,4*(village.m)//5,30)
tower4 = wizard_Tower(village.n//6,(village.m)//3,30)

hut1 =  Hut(village.n//4,village.m//4,40)
hut2 =  Hut(3*village.n//4,village.m//4,40)
hut3 =  Hut(village.n//4,3*village.m//4,40)
hut4 =  Hut(3*village.n//4,3*village.m//4,40)
hut5 =  Hut(village.n//2,3*village.m//4,40)



build = [townHall,hut1,hut2,hut3,hut4,hut5]
build1 = [townHall,hut1,hut2,hut3,hut4,hut5]
all_defence_build = [canon1,canon2,canon3,canon4,tower1,tower2,tower3,tower4]
defence_build =  []
def level(x):
    if(x==1):
        defence_build = all_defence_build[:2]+all_defence_build[4:6]
        build =build1+defence_build
    elif(x==2):
        defence_build = all_defence_build[:3]+all_defence_build[4:7]
        build =build1 + defence_build

    elif(x==3):
        defence_build = all_defence_build[:4]+all_defence_build[4:8]
        build = build1 + defence_build
    else:
        defence_build = all_defence_build[:4]+all_defence_build[4:8]
        build = build1 + defence_build

    return [defence_build,build]

def reset_build():
    for  i in build:
        i.current_health =i.health
        i.destroyed =0
    for j in walls:
        j.current_health =j.health
        j.destroyed =0       







#walls
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
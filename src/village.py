from sys import stdout
from colorama import Fore
from colorama import init as colorama_init
import copy
n= 30
m= 100
village= []
village_object=[]

def reset_village():
    village = []
    for i in range(n):
        arr=[]
        for j in range(m):
            arr.append(Fore.LIGHTWHITE_EX  + "\u2592")
            #print(Fore.LIGHTGREEN_EX + "\u2592",end="")
        village.append(arr)
    #print("")
    village_object = copy.deepcopy( village)
    return [village_object,village]
[village_object,village] =reset_village()


def display_Village():
    stdout.flush()
    for i in range(n):
        for j in range(m):
            print(village[i][j],end = "")
        print("")






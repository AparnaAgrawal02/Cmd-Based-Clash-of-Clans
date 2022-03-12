import src.troops as troops

class spell():
    def heal(self):
        if(not troops.k.dead):
            troops.k.current_health =troops.k.health if troops.k.current_health*1.5>troops.k.health else troops.k.current_health*1.5
        for b in troops.barb_obj:
            if(not b.dead):
                b.current_health = b.health if b.current_health*1.5>b.health else b.current_health*1.5

    def rage(self):
        if(not troops.k.dead):
           troops.k.step*=2
           troops.k.damage*=2
        for b in troops.barb_obj:
            if(not b.dead):
                b.step*=2
                b.damage*=2


    def which_spell(self,key):
        if(key == "h"or key =="H"):
            self.heal()
        elif(key == "r"or key =="R"):
            self.rage()


sp = spell()
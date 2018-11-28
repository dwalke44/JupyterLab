import random as rd

# HAVE TO RESTART .IPYNB KERNEL FOR CHANGES TO TAKE EFFECT

class bcolors:
    HEADER = '\022[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Person:
    #stats
    def __init__(self, hp, mp, atk, df, mag):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = mag
        self.actions = ["Attack", "Magic"]
        
    def generate_damage(self):
        return rd.randrange(self.atkl, self.atkh)
    
    def generate_spell_damage(self, i):
        magicl = self.magic[i]["dmg"] - 5
        magich = self.magic[i]["dmg"] + 5
        return rd.randrange(magicl, magich)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
import random as rd

# HAVE TO RESTART .IPYNB KERNEL FOR CHANGES TO TAKE EFFECT

class bcolors:
    HEADER = '\022[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' #command to end color manipulation options
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
    
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost
        
    def get_spell_name(self, i):
        return self.magic[i]["name"]
    
    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]
    
    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1
            
    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":",  spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1
            
            
        
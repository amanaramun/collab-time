# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:57:05 2024

@author: endro
"""


import random
import math
import numpy as np
import subprocess
import pandas as pd
subprocess.call("get_spell_information.py", shell=True)

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self,num_of_dice, out_come = None):
        self.num_of_dice = num_of_dice
        self.out_come = []
        for i in range(0,self.num_of_dice):
            self.out_come.append(random.randint(1,self.sides))
        #return print( f"rolling a {self.num_of_dice}d{self.sides} for" ,self.out_come)    
        return self.out_come
    def advantage(self):
        x = random.randint(1,self.sides)
        y = random.randint(1,self.sides)
        adv = max(x,y)
        print('die 1:', x,',die 2:', y, '     advantage:',adv) 
        
    def disadvntage(self):
        x = random.randint(1,self.sides)
        y = random.randint(1,self.sides)
        adv = min(x,y)
        print('die 1:', x,',die 2:', y, '     disadvantage:',adv)
        

            
class character_sheet:
    def __init__(self, STR, DEX, CON, INT, WIS,CHA, LEVEL, CLASS, HP):      
        #maybe add a list of proffencies,
        global counter
        self.counter = 0
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.LEVEL = LEVEL
        self.CLASS = CLASS
        self.HP = HP
    def proficiency_modifier(self):
        if self.CLASS == 'CLERIC':
            return ['WIS', 'CHA']
    def proficiency_by_level(self):
        if self.LEVEL < 5:
            return 2
        elif self.LEVEL < 9: 
            return 3
        elif self.LEVEL < 13:
            return 4
        elif self.LEVEL < 17:
            return 5
        else:
            return 6
    def STR_modifier(self):
        return math.floor((self.STR-10) /2)  
    def DEX_modifier(self):
        return math.floor((self.DEX-10) /2)    
    def CON_modifier(self):
        return math.floor((self.CON-10) /2)        
    def INT_modifier(self):
        return math.floor((self.INT-10) /2)    
    def WIS_modifier(self):
        return math.floor((self.WIS-10) /2)       
    def CHA_modifier(self):
        return math.floor((self.CHA-10) /2)    
    def current_level(self):
        return self.LEVEL
    def get_num_cantrips(self):
        return spell_slot_dict[self.LEVEL][0]
    def get_save_dc(self):
        return math.floor((self.WIS-10) /2) + 10 
    def get_spell_slots(self):
        if self.LEVEL > 20:
            return spell_slot_dict[20]   
        else:
            return spell_slot_dict[self.LEVEL]               
    def get_hp(self):
        return (self.HP)
    
    
    
    
'''    
    def current_hp(self):
        return self.HP     
    
    def take_damage(self, damage):
        self.damage = damage
        self.HP -= self.damage
        self.counter +=1
        return self.HP
'''
#make a class for couting spell slots
#maybe break this out so i can have a profience bonus for spell attacks too    
class ability_check:
    def __init__ (self, character):
        self.character = character
    def roll(self, modifier_stat,proficiency):
        self.proficiency = proficiency
        self.modifier_stat=modifier_stat
        ability_roll_check = Dice(20)
        roll = ability_roll_check.roll(1) 
        if roll[0] == 20:
            return print('NAT 20 bitches')
        elif roll[0] == 1:
            return print('NAT 1 :(')
        else:
            if self.modifier_stat == "STR" :
                if "STR" in self.character.proficiency_modifier() and self.proficiency == True:
                    prof = int(self.character.proficiency_by_level())
                else:
                    prof = 0
                bonus = self.character.STR_modifier()  + prof
            if self.modifier_stat == "DEX" :
                if "DEX" in self.character.proficiency_modifier() and self.proficiency == True:
                    prof = int(self.character.proficiency_by_level())
                else:
                    prof = 0
                bonus = self.character.DEX_modifier()  +  prof 
            if self.modifier_stat == "CON" :
                if "CON" in self.character.proficiency_modifier() and self.proficiency == True:
                    prof =int(self.character.proficiency_by_level())
                else:
                    prof = 0
                bonus = self.character.CON_modifier() +  prof 
            if self.modifier_stat == "INT":
                if "INT" in self.character.proficiency_modifier()  and self.proficiency == True:
                    prof = int(self.character.proficiency_by_level())
                else:
                    prof = 0
                bonus = self.character.INT_modifier()   +  prof 
            if self.modifier_stat == "WIS":
                if "WIS" in self.character.proficiency_modifier() and self.proficiency == True:
                    prof = int(self.character.proficiency_by_level())
                else:
                    prof = 0
                bonus = self.character.WIS_modifier() +  prof 
                    #you need to figure out how to do a profiency based on the object
            if self.modifier_stat == "CHA" :
                if "CHA" in self.character.proficiency_modifier() and self.proficiency == True:
                    prof = int(self.character.proficiency_by_level())
                else:
                    prof = 0
                bonus = self.character.CHA_modifier() + prof    
            return print(f"{self.modifier_stat} ability roll:",roll , "+ bonus modifier:",bonus,
                         ' = ',int(roll[0]) + int(bonus))
     


#print(fun)
#print(fun["Acid Splash"])

class get_info:
    def __init__(self, dictionary):
        self.dictioanry = dictionary
    def get_casting_time(self, name):
        self.name = name
        return self.dictioanry[self.name]['casting_time']    
    def get_school(self, name):
        self.name = name
        return self.dictioanry[self.name]['school']
    def get_duration(self, name):
        self.name = name
        return self.dictioanry[self.name]['duration']    
    def get_range(self, name):
        self.name = name
        return self.dictioanry[self.name]['range']    
    def get_ritual(self, name):
        self.name = name
        return self.dictioanry[self.name]['ritual']       
    def get_description(self, name):
        self.name = name
        return self.dictioanry[self.name]['description']    
    def get_higher_levels(self, name):
        self.name = name
        return self.dictioanry[self.name]['higher_levels']   
    def get_level(self, name):
        self.name = name
        return self.dictioanry[self.name]['level']
    def get_cast_higher(self, name):
        self.name = name
        return self.dictioanry[self.name]['cast_higher']  
    def get_concentration(self, name):
        self.name = name
        return self.dictioanry[self.name]['concentration']  
    
spells_list = pd.read_excel(r"C:\\Users\\endro\\Desktop\\Python or R\\d&d_stuff\\D&D 5E Spells.xlsx")

#cantrips = spells_list[spells_list['level'] == 0] 
#cantrips.columns



def get_attributes(name):
    print('')   
    print('******************༼ つ ◕_◕ ༽つ**************************')   
    print('     spell:', name)
    print('     base level:', info.get_level(name)) 
    print('     school:', info.get_school(name))
    print('     casting time:', info.get_casting_time(name))
    print('     concentration:', info.get_concentration(name))    
    print('     duration:', info.get_duration(name))
    print('     range:',info.get_range(name) )
    print('     ritual', info.get_ritual(name))
    print('     description:', info.get_description(name))    
    print('****************************************************')    
    print('')   
    
class cantrips:
    def __init__ (self, character):   
         self.character = character       
    def sacred_flame(self):
        damage=Dice(8)
        current_level =  self.character.current_level()
        if self.character.current_level()< 5:
            rolls = np.array(damage.roll(1))
            num_of_rolls = '1'
            total = rolls.sum() 
        elif self.character.current_level()< 11:
            rolls = np.array(damage.roll(2))
            num_of_rolls = '2'
            total = rolls.sum() 
        elif self.character.current_level()< 17:
            rolls = np.array(damage.roll(3))
            total = rolls.sum()     
            num_of_rolls = '3'
        else:
            rolls = np.array(damage.roll(4))
            total = rolls.sum() 
            num_of_rolls = '4'
        get_attributes('Sacred Flame')   
        return print(f" at level {current_level} rolls {num_of_rolls}d8 :", rolls, 'total:', total)     
    def guidance(self):
        damage=Dice(4)
        rolls = np.array(damage.roll(1))
        get_attributes('Guidance')   
        return print('rolls:', rolls)
    def light(self):
        get_attributes('Light')
    def mending(self):
        get_attributes('Mending')       
    def resistance(self):
        get_attributes('Resistance')   
    def spare_the_dying(self):
        get_attributes('Spare the Dying')   
    def thaumaturgy(self):
        get_attributes('Thaumaturgy')   
    def toll_the_dead(self, predamage):
        self.predamage = predamage
        current_level =  self.character.current_level()
        if self.predamage == True:
            damage = Dice(12)     
            type_of_dice = 'd12'
        else:
            damage = Dice(8)
            type_of_dice = 'd8'
        if self.character.current_level()< 5:
            rolls = np.array(damage.roll(1))
            num_of_rolls = '1'
            total = rolls.sum() 
        elif self.character.current_level()< 11:
            rolls = np.array(damage.roll(2))
            total = rolls.sum() 
            num_of_rolls = '2'
        elif self.character.current_level()< 17:
            rolls = np.array(damage.roll(3))
            total = rolls.sum()     
            num_of_rolls = '3'
        else:
            rolls = np.array(damage.roll(4))
            total = rolls.sum() 
            num_of_rolls = '4'
        get_attributes('Toll the Dead')   
        return print(f"at level {current_level} rolls {num_of_rolls}{type_of_dice}:", rolls, 'total:', total)   
    def word_of_radiance(self):
        current_level =  self.character.current_level()
        damage = Dice(6)
        if self.character.current_level()< 5:
            rolls = np.array(damage.roll(1))
            num_of_rolls = '1'
            total = rolls.sum() 
        elif self.character.current_level()< 11:
            rolls = np.array(damage.roll(2))
            num_of_rolls = '2'
            total = rolls.sum() 
        elif self.character.current_level()< 17:
            rolls = np.array(damage.roll(3))
            total = rolls.sum()     
            num_of_rolls = '3'
        else:
            rolls = np.array(damage.roll(4))
            total = rolls.sum() 
            num_of_rolls = '4'
        get_attributes('Word of Radiance')   
        return print(f"at level {current_level} rolls {num_of_rolls}d6:", rolls, 'total:', total)   


def out_of_point(rank):
            print('')   
            print('*******************<( ′□′)>───~~...**********************')
            print('********************(╯′□′)╯︵┻━┻*************************')
            print('      not enough spell points to cast at rank', rank)
            print('************************(°ロ°)****************************')
            print('*************************WOMP****************************')
            print('')   
            
class ranked_spells:
    def __init__ (self, character):
        self.character = character 
        global proficient
        if "WIS" in self.character.proficiency_modifier():
            proficient = int(self.character.proficiency_by_level())
        else:
             proficient =0  
    def guiding_bolt(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Guiding Bolt') + (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Guiding Bolt') + (self.rank -1))
            damage=Dice(6)
            rolls = np.array(damage.roll(4+self.rank-1))
            total = rolls.sum() 
            get_attributes('Guiding Bolt')
            print(f"rank {self.rank} rolls:", rolls, 'total:', total) 
    def cure_wounds(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Cure Wounds') + (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Cure Wounds') 
                                                 + (self.rank -1))
            damage=Dice(8)
            rolls = np.array(damage.roll(1+self.rank-1))
            bonus = self.character.WIS_modifier() +proficient
            total = rolls.sum() + bonus
            get_attributes('Cure Wounds')   
            print(f"rank {self.rank} rolls:", rolls, 'spell casting modifier:'
                 ,bonus ,  'total:', total)   
    def detect_evil_and_good(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Detect Evil and Good'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Detect Evil and Good')
    def detect_magic(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Detect Magic'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Detect Magic')
    def detect_poison_and_disease(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Detect Poison and Disease'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Detect Poison and Disease')
         
    def inflict_wounds(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Inflict Wounds') + (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Inflict Wounds') 
                                                 + (self.rank -1))
            damage=Dice(10)
            rolls = np.array(damage.roll(1+self.rank-1))
            #bonus = self.character.WIS_modifier() +proficient
            #total = rolls.sum() + bonus
            total = rolls.sum() 
            get_attributes('Inflict Wounds')   
            print(f"rank {self.rank} rolls:", rolls, 'total:', total)
    def healing_word(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Healing Word') + (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Healing Word') 
                                                 + (self.rank -1))
            damage=Dice(4)
            rolls = np.array(damage.roll(1+self.rank-1))
            bonus = self.character.WIS_modifier() +proficient
            total = rolls.sum() + bonus
            get_attributes('Healing Word')   
            print(f"rank {self.rank} rolls:", rolls, 'spell casting modifier:'
                 ,bonus ,  'total:', total)
            
    def create_or_destory_water(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Create Food and Water'))
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Create Food and Water') 
                                                + (self.rank -1))
            area = 30 + (info.get_level('Create Food and Water') + (self.rank -1) * 5)
            gallon = 10 + (info.get_level('Create Food and Water') + (self.rank -1) * 10)
            get_attributes('Create Food and Water') 
            print("Create or destory", gallon , "gallons of water or", area, 'sq foot of water')

    def protection_from_evil_and_good(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Protection from Evil and Good'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Protection from Evil and Good')
    def purify_food_and_drink(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Purify Food and Drink'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Purify Food and Drink')   
    def sanctuary(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Sanctuary'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Sanctuary')   
    def shield_of_faith(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Shield of Faith'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Shield of Faith')   
    def ceremony(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Ceremony'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Ceremony')   
    def command(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Command')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Command')+ (self.rank -1))
          damage = 1 + (int(self.rank -1))*1
          get_attributes('Command')   
          print(f"rank {self.rank} targets ",damage ,  "creatures")                  
    def bless(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Bless')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Bless')+ (self.rank -1))
          damage = 1 + (int(self.rank -1))*1
          get_attributes('Bless')   
          print(f"rank {self.rank} blesses ",damage ,  "creatures")                
    def aid(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Aid')+ (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Aid')+ (self.rank -1))
            damage = 5 + (int(self.rank -1))*5
            get_attributes('Aid')   
            print(f"rank {self.rank} heals 3 taregets for:", damage) 
    def augury(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Augury'))
        else:
            avaliable_spell_slots.use_spell_slot(2)
            get_attributes('Augury')               
    def blindness_deafness(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Blindness/Deafness')+ (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Blindness/Deafness')+ (self.rank -1))
            damage = 1 + (int(self.rank -1))*1
            get_attributes('Blindness/Deafness')   
            print(f"rank {self.rank} blinds or deafens ",damage ,  "taregets")             
    def continual_flame(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Continual Flame'))
        else:
            avaliable_spell_slots.use_spell_slot(2)
            get_attributes('Continual Flame')        
    def enhance_ability(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Enhance Ability'))
        else:
            avaliable_spell_slots.use_spell_slot(2)
            get_attributes('Enhance Ability')      
    def bane(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Bane')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Bane')+ (self.rank -1))
          if self.rank == 1:
              damage=1  
          elif self.rank >1:
              damage = 1 + (int(self.rank -1))*1
          get_attributes('Bane')   
          print(f"rank {self.rank} targets",damage ,  "creatures")    
    def find_traps(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Find Traps'))
        else:
            avaliable_spell_slots.use_spell_slot(2)
            get_attributes('Find Traps')      
    def gentle_repose(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Gentle Repose'))
        else:
            avaliable_spell_slots.use_spell_slot(2)
            get_attributes('Gentle Repose')          
            
    def hold_person(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Hold Person')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Hold Person')+ (self.rank -1))
          damage = 1 + (int(self.rank -1))*1
          get_attributes('Hold Person')   
          print(f"rank {self.rank} holds ",damage ,  "humanoids")
    def lesser_restoration(self,rank):
       self.rank = 1
       current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
       if current <= 0:
           out_of_point(info.get_level('Lesser Restoration'))
       else:
           avaliable_spell_slots.use_spell_slot(2)
           get_attributes('Lesser Restoration')
    def locate_object(self,rank):
        self.rank = 1
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Locate Object'))
        else:
            avaliable_spell_slots.use_spell_slot(2)
            get_attributes('Locate Object')
    def prayer_of_healing(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Prayer of Healing') + (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Prayer of Healing') 
                                                 + (self.rank -1))
            damage=Dice(8)
            rolls = np.array(damage.roll(2+self.rank-1))
            bonus = self.character.WIS_modifier() 
            total = rolls.sum() + bonus
            get_attributes('Prayer of Healing')   
            print(f"rank {self.rank} heals 6 creatures for:", rolls, 'spell casting modifier:'
                 ,bonus ,  'total:', total) 
    def protection_from_poison(self,rank):
        self.rank = 2
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Protection from Poison'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Protection from Poison')   
    def silence(self,rank):
        self.rank = 2
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Silence'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Silence')   
    def spiritual_weapon(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Spiritual Weapon') + (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Spiritual Weapon') 
                                                 + (self.rank -1))
            damage=Dice(8)
            rolls = np.array(damage.roll(1+math.floor(self.rank/2)))
            total = rolls.sum() 
            get_attributes('Spiritual Weapon')   
            print(f"rank {self.rank} rolls:", rolls, 'total:', total) 

    def warding_bond(self,rank):
        self.rank = 2
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Warding Bond'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Warding Bond')   
			
    def zone_of_truth(self,rank):
        self.rank = 2
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Zone of Truth'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Zone of Truth')   
    def borrowed_knowledge(self,rank):
        self.rank = 2
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Borrowed Knowledge'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Borrowed Knowledge')   

    def beacon_of_hope(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Beacon of Hope'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Beacon of Hope')   
			
  
    def clairvoyance(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Clairvoyance'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Clairvoyance')   
			
    def create_food_and_water(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Create Food and Water'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Create Food and Water')   
			
    def daylight(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Daylight'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Daylight')      
			
    def feign_death(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Feign Death'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Feign Death')       
			
			
    def meld_into_stone(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Meld into Stone'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Meld into Stone')     

    def protection_from_energy(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Protection from Energy'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Protection from Energy')  

    def remove_curse(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Remove Curse'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Remove Curse')      

			
    def revivify(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Revivify'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Revivify')      	
			
    def sending(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Sending'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Sending')      	
			
    def speak_with_dead(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Speak with Dead'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Speak with Dead')      						
						
						
    def tongues(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Tongues'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Tongues')     
			
    def water_walk(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Water Walk'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Water Walk')  			

						
    def incite_greed(self,rank):
        self.rank = 3
        current = int(avaliable_spell_slots.get_current_spell_slots()[self.rank] )
        if current <= 0:
            out_of_point(info.get_level('Incite Greed'))
        else:
            avaliable_spell_slots.use_spell_slot(1)
            get_attributes('Incite Greed')     	


    def animate_dead(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Animate Dead')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Animate Dead')+ (self.rank -1))
          damage = 1 + (int(self.rank -1))*1
          get_attributes('Animate Dead')  
          if self.rank > 1:
              print(info.get_higher_levels('Animate Dead'))
          print(f"rank {self.rank} animates ",damage ,  "minions")		               
    def bestow_curse(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Bestow Curse')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Bestow Curse')+ (self.rank -1))
          get_attributes('Bestow Curse')  
          if self.rank > 1:
              print(info.get_higher_levels('Bestow Curse'))
    def dispel_magic(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Dispel Magic')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Dispel Magic')+ (self.rank -1))
          get_attributes('Dispel Magic')  
          if self.rank > 1:
              print(info.get_higher_levels('Dispel Magic'))
    def glyph_of_warding(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Glyph of Warding')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Glyph of Warding')+ (self.rank -1))
          get_attributes('Glyph of Warding')  
          if self.rank > 1:
              print(info.get_higher_levels('Glyph of Warding'))      
    def magic_circle(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Magic Circle')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Magic Circleg')+ (self.rank -1))
          get_attributes('Magic Circle')  
          if self.rank > 1:
              print(info.get_higher_levels('Magic Circle'))
               
    def mass_healing_word(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Mass Healing Word') + (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Mass Healing Word') 
                                                 + (self.rank -1))
            damage=Dice(4)
            rolls = np.array(damage.roll(1+self.rank-1))
            bonus = self.character.WIS_modifier() +proficient
            total = rolls.sum() + bonus
            get_attributes('Mass Healing Word')   
            print(f"rank {self.rank} heals 6 creatures for:", rolls, 'spell casting modifier:'
                 ,bonus ,  'total:', total)                                         
    def spirit_guardians(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Spirit Guardians')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Spirit Guardians')+ (self.rank -1))
          get_attributes('Spirit Guardians')  
          if self.rank > 1:
              print(info.get_higher_levels('Spirit Guardians'))  
    def spirit_shroud(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Spirit Shroud') + (self.rank -1)] )
        if current <= 0:
            out_of_point(self.rank)
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Spirit Shroud') 
                                                 + (self.rank -1))
            damage=Dice(8)
            rolls = np.array(damage.roll(1+math.floor(self.rank/2)))
            total = rolls.sum() 
            get_attributes('Spirit Shroud')   
            print(f"rank {self.rank} rolls:", rolls, 'total:', total)                           
    def fast_friends(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Fast Friends')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Fast Friends')+ (self.rank -1))
          damage = 1 + (int(self.rank -1))*1
          get_attributes('Fast Friends')   
          print(f"rank {self.rank} befriends ",damage ,  "humanoids") 
    def motivational_speech(self,rank):
      self.rank = rank
      current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Motivational Speech')+ (self.rank -1)] )
      if current <= 0:
          out_of_point(self.rank)
      else:
          avaliable_spell_slots.use_spell_slot(info.get_level('Motivational Speech')+ (self.rank -1))
          damage = 5 + (int(self.rank -1))*5
          get_attributes('Motivational Speech')   
          print(f"rank {self.rank} 5 targets gains temporary health points:", damage) 
          
          
          ## this is not working##
          
        
          
          
    def banishment(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Banishment')+ (self.rank -1)] )
        if current <= 0:
            out_of_point(info.get_level('Banishment'))
        else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Banishment')+ (self.rank -1))
            get_attributes('Banishment')     
            
    def control_water(self,rank):
        self.rank = rank
        current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Control Water')+ (self.rank -1)] )
        if current <= 0:
            out_of_point(info.get_level('Control Water'))
        else:
             avaliable_spell_slots.use_spell_slot(info.get_level('Control Water')+ (self.rank -1))
             get_attributes('Control Water')        
             
             
    def death_ward(self,rank):
       self.rank = rank
       current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Death Ward')+ (self.rank -1)] )
       if current <= 0:
           out_of_point(info.get_level('Death Ward'))
       else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Death Ward')+ (self.rank -1))
            get_attributes('Death Ward')        

            
    def divination(self,rank):
       self.rank = rank
       current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Divination')+ (self.rank -1)] )
       if current <= 0:
           out_of_point(info.get_level('Divination'))
       else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Divination')+ (self.rank -1))
            get_attributes('Divination')  
            
    def freedom_of_movement(self,rank):
       self.rank = rank
       current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Freedom of Movement')+ (self.rank -1)] )
       if current <= 0:
           out_of_point(info.get_level('Freedom of Movement'))
       else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Divination')+ (self.rank -1))
            get_attributes('Freedom of Movement')  
            
    def guardian_of_faith(self,rank):
       self.rank = rank
       current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Guardian of Faith')+ (self.rank -1)] )
       if current <= 0:
           out_of_point(info.get_level('Guardian of Faith'))
       else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Divination')+ (self.rank -1))
            get_attributes('Guardian of Faith')  
            
    def locate_creature(self,rank):
       self.rank = rank
       current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Locate Creature')+ (self.rank -1)] )
       if current <= 0:
           out_of_point(info.get_level('Locate Creature'))
       else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Locate Creature')+ (self.rank -1))
            get_attributes('Locate Creature')  
            
    def stone_shape(self,rank):
       self.rank = rank
       current = int(avaliable_spell_slots.get_current_spell_slots()[info.get_level('Stone Shape')+ (self.rank -1)] )
       if current <= 0:
           out_of_point(info.get_level('Stone Shape'))
       else:
            avaliable_spell_slots.use_spell_slot(info.get_level('Stone Shape')+ (self.rank -1))
            get_attributes('Stone Shape')  

                  
class spell_status:
    def __init__(self, character):
        self.character = character
        global current_slots
        current_slots =  self.character.get_spell_slots()
    def use_spell_slot(self, rank):
        self.rank = rank
        current_slots[self.rank] -=1
        return     
    def get_current_spell_slots(self):
        return current_slots
    def get_current_spell_slots_status(self):
        if self.character.current_level() > 9:
            print('')   
            print('*********************¯\(°_o)/¯***********************')
            print('current avaialbe spell slots at level: ', self.character.current_level())
            for i in range(1,10):
                print("rank",i,':', current_slots[i])      
            print('*****************************************************')               
            print('')   
        else:
            print('')   
            print('*********************¯\(°_o)/¯***********************')
            print('current avaialbe spell slots at level: ', self.character.current_level())
            for i in range(1,math.ceil(self.character.current_level()/2)+1):
                print("rank",i,':', current_slots[i]) 
            print('*****************************************************')   
            print('')   

def level_up_hp():    
    current_hp = int(kazuma.get_hp())
    hp_level = Dice(8)
    on_level_up= int(hp_level.roll(1)[0])
    con = int(kazuma.CON_modifier()) ;
    new_hp = current_hp + on_level_up + con
    print('current hp:', current_hp, ' HP roll:', on_level_up, "Consitution_modifier", kazuma.CON_modifier(), 'new HP:' ,new_hp)      

#list of all spells;
spells = spells_list.set_index("name").T.to_dict()    
info = get_info(spells)


#list of spell slots by level
spell_slot_total = pd.read_excel(r"C:\\Users\\endro\\Desktop\\Python or R\\d&d_stuff\\cleric spell slots.xlsx")
spell_slot_dict = spell_slot_total.set_index("Level").T.to_dict("list")


kazuma = character_sheet(STR= 7
                         ,DEX = 13
                         ,CON = 16
                         ,INT = 9
                         ,WIS = 20 
                         ,CHA = 16
                         ,LEVEL = 7
                         ,CLASS = 'CLERIC'
                         ,HP = 65)

avaliable_spell_slots = spell_status(kazuma)
ability_roll = ability_check(kazuma)
cast_cantrip = cantrips(kazuma)

cast_spell = ranked_spells(kazuma)

avaliable_spell_slots.get_current_spell_slots_status()
#print(kazuma.WIS_modifier())
#print(kazuma.STR_modifier())
#print(kazuma.current_level())
#print(kazuma.current_level())
#(kazuma.proficiency_by_level())
#print(kazuma.get_num_cantrips())
#print(kazuma.get_spell_slots())

'''
other things to write
atheletic chiecks and other skill based rolls
weapon attacks
hp counter
rest of the skills
'''
#current HP: 21+25

# 
d3 = Dice(3)
d100 = Dice(100)
d20 = Dice(20)
d12 = Dice(12)
d10 = Dice(10)
d8 = Dice(8)
d6 = Dice(6)
d4 = Dice(4)
d36 = Dice(36)
level_up_hp()   
#once you write the spell slot counter you can use the method to do HP too for leveling up

'''roll section'''


#for i in range(0,100):
#    print(d.roll())
d3.roll(1)
d4.roll(1)
d6.roll(1)
d8.roll(2)
d12.roll(1)
d20.roll(1)
d36.roll(1)
d20.roll(1)
d100.roll(2)

#roll 5d20
d20.advantage()
d20.disadvntage()
#d8.advantage()

ability_roll.roll(modifier_stat = "STR"
                  , proficiency = False)

ability_roll.roll(modifier_stat = "WIS"
                  , proficiency = False)
ability_roll.roll(modifier_stat = "WIS"
                  , proficiency = True)

ability_roll.roll(modifier_stat = "CHA"
                  , proficiency = False)

ability_roll.roll(modifier_stat = "CHA"
                  , proficiency = False)

ability_roll.roll(modifier_stat = "DEX"
                  , proficiency = False)

ability_roll.roll(modifier_stat = "CON"
                  , proficiency = False)

ability_roll.roll(modifier_stat = "INT"
                  , proficiency = False)
ability_roll.roll(modifier_stat = "INT"
                  , proficiency = True)

#write an atheletics roll class.
#write a weapons attack class
#write a leanred skill class
#write a roll for iniative function, use Dice() method and add dex bonus
#1 emralds
# gay spear
    # verstile 1d6 1d8 pericing throw it comes +1 to atack and damage
    # hit creatuers take 1d6 necro damage and get half of hp back
    # spell casting focusing 
    # once per long rest i can turn radiant damage to necrotic and coverted 
    # damage half to temp hp work
# one trident of https://www.dndbeyond.com/magic-items/4784-trident-of-fish-command
#2640 gold

print(spell_slot_dict[7])
'''cantrip section'''
#
#cast_cantrip.mending()
cast_cantrip.resistance()
cast_cantrip.sacred_flame()
cast_cantrip.guidance()
#cast_cantrip.light()
cast_cantrip.spare_the_dying()
#cast_cantrip.thaumaturgy()
cast_cantrip.toll_the_dead(predamage = True)
cast_cantrip.toll_the_dead(predamage = False)


#Cleric Level	Spells
#1st	Bless, Cure Wounds
#3rd	Lesser Restoration, Spiritual Weapon
#5th	Beacon of Hope, Revivify
#7th	Death Ward, Guardian of Faith
#9th	Mass Cure Wounds, Raise Dead

#number of spells:  level + 5
#https://www.dndbeyond.com/magic-items/4684-necklace-of-prayer-beads
 #bless
#cure wounds
d8.roll(2)
#Greater restoration
#Wind Walk 
#https://www.dndbeyond.com/spells/2301-wind-walk
#without summons
 
#disciple of LifePHB, pg. 60
#Also starting at 1st level, 
#your healing spells are more effective.
# Whenever you use a spell of 1st level or 
#higher to restore hit points to a creature
#, the creature regains additional hit 
#points equal to 2 + the spell’s level.
#10 hobos scarfcied. 

print(spell_slot_dict[7])
print(kazuma.get_save_dc())
#RANK 1:4-1 
#RANK 2:3
#RANK 3:3
#RANK 4:1

'''spell section'''
#make a spell slot counter before you do spells so you can add a counter to it
avaliable_spell_slots.get_current_spell_slots_status()
''' rank 1 spells'''
cast_spell.ceremony(rank = 1)
#cast_spell.command(rank = 1)
cast_spell.create_or_destory_water(rank = 3)
#cast_spell.detect_evil_and_good(rank = 1)
#cast_spell.detect_magic(rank = 1)
#cast_spell.detect_poison_and_disease(rank = 1)
#cast_spell.inflict_wounds(rank= 1)
#cast_spell.protection_from_evil_and_good(rank = 1)
cast_spell.shield_of_faith(rank = 1)
cast_spell.bless(rank =1) #always prepared
cast_spell.cure_wounds(rank = 1) #always prepared
cast_spell.guiding_bolt(rank = 1)

#cast_spell.purify_food_and_drink(rank = 1)

''' rank 1 bonus'''
#cast_spell.healing_word(rank= 1)
cast_spell.shield_of_faith(rank = 1)
#cast_spell.sanctuary(rank = 1)


'''rank 2 spell'''
#cast_spell.aid(rank = 2)
#cast_spell.augury(rank = 1)
#cast_spell.bane(rank = 1)
cast_spell.blindness_deafness(rank = 1)
#cast_spell.continual_flame(rank = 1)
#cast_spell.find_traps(rank = 1)
#cast_spell.gentle_repose(rank = 1)
cast_spell.hold_person(rank = 3)

#cast_spell.locate_object(rank = 1)
#cast_spell.protection_from_poison(rank = 1)
cast_spell.silence(rank = 1)
#cast_spell.enhance_ability(rank = 1)
cast_spell.lesser_restoration(rank = 1) #always prepared
cast_spell.prayer_of_healing(rank = 2)
''' rank 2 bonus'''
cast_spell.spiritual_weapon(rank = 2) #always prepared

'''rank 3 spell'''
#cast_spell.animate_dead(rank = 2)
cast_spell.beacon_of_hope(rank = 1) #always prepared
#cast_spell.bestow_curse(rank = 1)
#cast_spell.clairvoyance(rank = 1)
#cast_spell.create_food_and_water(rank = 1)
cast_spell.daylight(rank = 1)
#cast_spell.fast_friends(rank = 1)
cast_spell.feign_death(rank = 1)
#cast_spell.glyph_of_warding(rank = 1)
#cast_spell.magic_circle(rank = 1)
#cast_spell.mass_healing_word(rank = 1)
#cast_spell.meld_into_stone(rank = 1)
#cast_spell.motivational_speech(rank = 1)
#cast_spell.protection_from_energy(rank = 1)
cast_spell.remove_curse(rank = 1)
cast_spell.revivify(rank = 1) #always prepared
#cast_spell.sending(rank = 1)
#cast_spell.speak_with_dead(rank = 1)
#cast_spell.spirit_guardians(rank = 1)
#cast_spell.spirit_shroud(rank = 1)
#cast_spell.tongues(rank = 1)
cast_spell.water_walk(rank = 1)

'''rank 4 spell'''
#cast_spell.banishment(rank = 1)
#cast_spell.control_water(rank = 1)
cast_spell.death_ward(rank = 1) #always prepared
#cast_spell.divination(rank = 1)
#cast_spell.freedom_of_movement(rank = 1)
cast_spell.guardian_of_faith(rank = 1) #always prepared
#cast_spell.locate_creature(rank = 1)
#cast_spell.stone_shape(rank = 1)



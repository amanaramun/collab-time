# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:45:42 2024

@author: endro
"""
class spell:
    def __init__ (self, character):
        self.character = character
    def guiding_bolt(self,level):
        self.level = level
        damage=Dice(6)
        rolls = np.array(damage.roll(4+self.level-1))
        total = rolls.sum() +self.character.WIS_modifier()
        return rolls, self.character.WIS_modifier(), total
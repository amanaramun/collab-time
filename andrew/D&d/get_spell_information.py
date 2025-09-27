# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 08:57:50 2024

@author: endro
"""
import pandas as pd
spells_list = pd.read_excel(r"C:\\Users\\endro\\Desktop\\Python or R\\d&d_stuff\\D&D 5E Spells.xlsx")
spells = pd.DataFrame(spells_list)
#
test = spells[(spells['classes'].str.contains('Cleric')) ] 
test.to_excel('C:\\Users\\endro\\Desktop\\Python or R\\d&d_stuff\\cleric skills_all.xlsx')
test.head()
test.columns

test = spells_list.set_index("name").T.to_dict()
list(test.keys())

#print(fun)
print(test["Acid Splash"])

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
info = get_info(test)
info.get_school('Vortex Warp')
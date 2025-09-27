import pandas as pd
spell_slot_total = pd.read_excel(r"C:\\Users\\endro\\Desktop\\Python or R\\d&d_stuff\\cleric spell slots.xlsx")
spell_slot_dict = spell_slot_total.set_index("Level").T.to_dict("list")



class spell_status:
    def __init__(self, character):
        self.character = character
        global current_slots
        current_slots =  self.chracter.get_spell_slots(char_level = self.chracter.get_level())
    def use_spell_slot(self, spell_name, rank):
        current_slots[self.rank] -=1
        if  current_slots[self.rank] == 0:
            print("not enough spell slots to cast ", spell_name, 'at rank ', rank)
        else:
            return current_slots




'''
class GameStatus:
    def __init__(self):
        self.health = 100
    def reduce_health(self):
        self.health -= 10
        if self.health <= 0:
            game_over()
'''
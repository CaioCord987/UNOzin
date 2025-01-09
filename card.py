import random 

class Card:
    
    possible_colors = ['Red', 'Blue', 'Yellow', 'Green']
    possible_numbers = list(range(0, 10))

    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    @classmethod
    def create_random_card(cls):
        color = random.choice(cls.possible_colors)
        number = random.choice(cls.possible_numbers)
        new_card = cls(color, number)
        return new_card
      


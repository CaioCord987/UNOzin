from card import Card

class GameRules:

    def __init__(self):
        pass 

    last_played_card = None

    @classmethod
    def create_first_card(cls):
        cls.last_played_card = Card.create_random_card()

    @classmethod    
    def set_last_played_card(cls, card):
        cls.last_played_card = card


        

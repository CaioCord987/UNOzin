from card import Card
from game_rules import GameRules

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def add_random_card(self):
        self.hand.append(Card.create_random_card())
    
    def show_hand(self):
        print(f'{self.name} has the following cards:')
        for i in range(len(self.hand)):
            print(f'{i+1}- {self.hand[i].color}, {self.hand[i].number}')
    
    def select_card(self):
        while True:
            try: 
                card_number = int(input('What card would you like to play? Input 0 to draw a card. '))
                if card_number == 0:
                    return card_number
                if card_number < 1 or card_number > len(self.hand):
                    print('select a valid number.')
                    continue
                return self.hand[card_number-1]                     
            except ValueError:
                print('select a valid number.')

    def play_card(self): 
        while True:
            selected_card = Player.select_card(self)
            if selected_card == 0:   
                Player.add_random_card(self)
                print(f'You drew a {self.hand[len(self.hand)-1].color} {self.hand[len(self.hand)-1].number}')
                return
            if selected_card.color != GameRules.last_played_card.color and selected_card.number != GameRules.last_played_card.number:
                print('that card cannot be played, please select a valid card.')
                continue
            break
        GameRules.set_last_played_card(selected_card) 
        self.hand.remove(selected_card)

    def player_turn(self):
        Player.show_hand(self)
        Player.play_card(self)
                
    #play a card if possible, or draw
    def bot_play_a_card(self):    
        for card in self.hand:
            if card.color == GameRules.last_played_card.color or card.number == GameRules.last_played_card.number:
                print(f'{self.name} played a {card.color} {card.number}')
                GameRules.last_played_card = card
                self.hand.remove(card)
                return
        Player.add_random_card(self)
        print(f'{self.name} drew a card')

    def bot_turn(self):
        print(f'{self.name} has {len(self.hand)} card(s).')
        Player.bot_play_a_card(self)
        if len(self.hand) == 1:
            print('UNO!')

                
                

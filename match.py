from player import Player
from game_rules import GameRules
from card import Card 

GameRules.create_first_card()

p1 = Player(input('What is your name? '))
p2 = Player(input('What is your friend 1 name? '))
p3 = Player(input('What is your friend 2 name? '))
p4 = Player(input('What is your friend 3 name? '))

for i in range(5):
    p1.hand.append(Card.create_random_card())   
for i in range(5):
    p2.hand.append(Card.create_random_card())  
for i in range(5):
    p3.hand.append(Card.create_random_card())     
for i in range(5):
    p4.hand.append(Card.create_random_card())  

while True:
    print(f'Curently, the card on top is {GameRules.last_played_card.color} {GameRules.last_played_card.number}')
    Player.player_turn(p1)
    if len(p1.hand) == 0:
        print(f'{p1.name} has won!')
        break
    print(f'Curently, the card on top is {GameRules.last_played_card.color} {GameRules.last_played_card.number}')
    Player.bot_turn(p2)
    if len(p2.hand) == 0:
        print(f'{p2.name} has won!')
        break
    print(f'Curently, the card on top is {GameRules.last_played_card.color} {GameRules.last_played_card.number}')
    Player.bot_turn(p3)
    if len(p3.hand) == 0:
        print(f'{p3.name} has won!')
        break   
    print(f'Curently, the card on top is {GameRules.last_played_card.color} {GameRules.last_played_card.number}')
    Player.bot_turn(p4)
    if len(p4.hand) == 0:
        print(f'{p4.name} has won!')
        break


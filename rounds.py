import random
from typing import List

def play_round():
    # Create a card array ✔
    # Create arrays for player and computer ✔
    possible_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []

    # Choose a random card ✔
    # Choose 2 random cards for player ✔
    
    for i in range(2):
        player_cards.append(random.choice(possible_cards))
    
    return player_cards
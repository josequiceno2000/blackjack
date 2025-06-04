import random
from typing import List

possible_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def hit_or_stand():
    return input("Hit (get another card) or stand (keep current score)? Type 'h' or 's':\n> ").lower()

def hit(player_cards: List[int], player_score: int, computer_cards: List[int]):
    card_to_add = random.choice(possible_cards)
    player_cards.append(card_to_add)
    player_score += card_to_add
    print(f"\t\tYour cards: {player_cards}, current score: {player_score}")
    return player_cards, player_score

def stand(player_cards: List[int], player_final_score: int, computer_cards: List[int]):
    computer_final_score = sum(computer_cards)

    while computer_final_score < 17:
        computer_cards.append(random.choice(possible_cards))
        computer_final_score = sum(computer_cards)
    
    print(f"\t\tYour final hand: {player_cards}, final score: {player_final_score}")
    print(f"\t\tOpponent's final hand: {computer_cards}, final score: {computer_final_score}")

    if computer_final_score > 21:
        print("OPPONENT BUSTED - You win!")
        return

    if player_final_score == computer_final_score:
        print("PUSH - You tied!")
    elif player_final_score > computer_final_score:
        if player_final_score == 21:
            print("BLACKJACK - You won!")
        else:
            print("WIN - You won!")
    elif computer_final_score > player_final_score:
        print("LOWER HAND - You lost.")


def play_round():
    player_cards = []
    computer_cards = []

    for i in range(2):
        player_cards.append(random.choice(possible_cards))
    player_score = sum(player_cards)

    computer_cards.append(random.choice(possible_cards))

    print(f"\t\tYour cards: {player_cards}, current score: {player_score}")
    print(f"\t\tOpponent's card: {computer_cards}")
    
    return (player_cards, player_score, computer_cards)
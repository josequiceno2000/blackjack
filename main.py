from intro import play_blackjack, title_card
from rounds import play_round

def main():
    if play_blackjack():
        title_card()
        player_cards, computer_cards = (play_round())
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards}")

if __name__ == "__main__":
    main()
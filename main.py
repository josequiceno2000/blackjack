from intro import play_blackjack, title_card
from rounds import play_round, hit_or_stand, hit, stand

def main():
    while play_blackjack():
        title_card()
        player_cards, player_score, computer_cards = play_round()
        

        while player_score <= 21:
            user_choice = hit_or_stand()

            if user_choice == "h":
                player_cards, player_score = hit(player_cards, player_score, computer_cards)
            elif user_choice == "s":
                stand(player_cards, player_score, computer_cards)
                break
        
        if player_score == 21:
            stand(player_cards, player_score, computer_cards)
            
        if player_score > 21:
            print(f"BUST! You lost.")
        
        

if __name__ == "__main__":
    main()
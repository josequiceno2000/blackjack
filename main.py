from intro import play_blackjack, title_card
from rounds import play_round

def main():
    if play_blackjack():
        title_card()
        print(play_round())

if __name__ == "__main__":
    main()
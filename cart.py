import random
import string
import datetime


    #Name player
playerName = str(input())
    #Age player
playerAge = int(input())

    #Enter suit and cards
enter_suit = str(input())
enter_cards = str(input())

    #Suit cards array
suit_cards = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    #Cards array
cards = ['Ace', 'King', 'Queen', 'Jack', 'Joker']


    #Age < 18
if playerAge < 18:
    for j in range(5):
        print("|Error: Sorry you age less 18|")
    #Age > 18
elif playerAge > 18:
    print("==========================")
    print("Hello, " + playerName + "!")
    print("==========================\n\n")


        #Similarity check
    if (
            enter_suit == suit_cards[0] or enter_suit == suit_cards[1] or enter_suit == suit_cards[2] or enter_suit == suit_cards[3] and
            enter_cards == cards[0] or enter_cards == cards[1] or enter_cards == cards[2] or enter_cards == cards[3] or enter_cards == cards[4]
        ):
            print("You suit - " + enter_suit)
            print("Your cards - " + enter_cards)

                #Random element array
            rand_card = random.choice(cards)

                #Guessing condition
            if enter_cards != rand_card:
                print("\nWRONG,WRONG, AND WRONG!")
            else:
                print("\nYOU GUESSED IT A CARD!")
    else:
        print("There is no such card or suit!")

import random

money = 100
current_balance1 = money
current_balance2 = money

def card_game(bet, guess):
    global current_balance1
    global current_balance2
    print("Playing cards now!! The largest number wins. Players picked cards: ")
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck1 = random.choice(list)
    deck2 = random.choice(list)

    if deck1 > deck2:
        print(deck1)
        print(deck2)
        current_balance1 += bet
        current_balance2 -= bet

        return "The winner is player 1. Balance for player 1 is " + str(current_balance1) + ". " + "Balance for player 2 " + str(current_balance2) + ". "

    if deck2 > deck1:
        print(deck1)
        print(deck2)
        current_balance1 += bet
        current_balance2 -= bet

        return "The winner is player 2. Balance for player 2 is " + str(current_balance2) + ". " + "Balance for player 1 " + str(current_balance1) + ". "

    if deck1 == deck2:
        print(deck1)
        print(deck2)

        return "Tie, so no winner."
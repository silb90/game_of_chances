import random

money = 100
current_balance1 = money
current_balance2 = money

def card_game(bet, guess):
    global current_balance1
    global current_balance2
    deck1 = random.choice([1, 13, 1])
    deck2 = random.choice([1, 13, 1])

    if deck1 > deck2:
        current_balance1 += bet
        current_balance2 -= bet

        return "The winner is player 1. Balance for player 1 is " + current_balance1 + ". " + "Balance for player 2 " + current_balance2 + ". "

    if deck2 > deck1:
        current_balance1 += bet
        current_balance2 -= bet

        return "The winner is player 2. Balance for player 2 is " + current_balance2 + ". " + "Balance for player 1 " + current_balance1 + ". "

    if deck1 == deck2:

        return "Tie, so no winner."
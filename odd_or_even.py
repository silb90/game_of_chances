

import random

money = 100
current_balance = 100

def odd_or_even(bet, guess):
    global current_balance
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    dice2 = random.choice([1, 2, 3, 4, 5, 6])

    sum = dice1 + dice2

    if sum%2 == 0 and guess == "Even":
        current_balance += bet
        return "You win! The sum is " + str(sum) + " and you bet even."
    elif sum%2 == 0 and guess == "Odd":
        current_balance -= bet
        return "You lose! The sum is " + str(sum) + " and you bet odd."
    elif sum%2 != 0 and guess == "Even":
        return "You lose! The sum is " + str(sum) + " and you bet even."
    elif sum%2 != 0 and guess == "Odd":
        return "You win! The sum is " + str(sum) + " and you bet odd."


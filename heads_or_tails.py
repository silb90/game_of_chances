import random

money = 100
current_balance = money

def heads_or_tails(bet, guess):
    global current_balance

    print("Heads or tails?")
    flip = random.choice([1, 2])
    print(flip)
    if guess == 1 and flip == 1:
        current_balance += bet
        return "Heads. You win! Your current balance is " + str(current_balance)

    elif guess == 1 and flip == 2:
        current_balance -= bet
        return "Heads. You lose! Your current balance is " + str(current_balance)

    elif guess == 2 and flip == 2:
        current_balance += bet
        return "Tails. You win! Your current balance is " + str(current_balance)

    else:
        current_balance -= bet
        return "Tails. You lose! Your current balance is " + str(current_balance)


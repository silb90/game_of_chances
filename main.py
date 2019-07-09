import random

money = 100

def heads_or_tails(bet, guess):
    flip = random.choice([1, 2])
    print(flip)
    if guess == 1 and flip == 1:
        current_balance = money + bet
        return "Heads. You win! Your current balance is " + str(current_balance)
    elif guess == 1 and flip == 2:
        current_balance = money - bet
        return "Heads. You lose! Your current balance is " + str(current_balance)
    elif guess == 2 and flip == 2:
        current_balance = money + bet
        return "Tales. You win! Your current balance is " + str(current_balance)
    else:
        current_balance = money - bet
        return "Tales. You lose! Your current balance is " + str(current_balance)


result = heads_or_tails(30, 2)

print(result)

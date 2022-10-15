import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while random_num != guess:
        guess = int(input(f"Guess a number between 1 and {x} : "))
        if guess < random_num:
            print("Too low, guess again")
        elif guess > random_num:
            print("Too high, guess again")
    print(f"Yay! you guessed it right. The number is {random_num}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high: 
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)").lower()
        if  feedback == 'h':
            high = guess - 1 
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess} correctly!!')



limit = int(input("Enter the limit of the guessing game : "))
choice = input("How would you like to play the game ? Will you participate(P) or contest the game (C)").lower()
if choice == 'p':
    print(f"Get ready to guess! between 1 and {limit}")
    guess(limit)
else:
    print(f"Ready with a number between 1 and {limit}")
    computer_guess(limit)
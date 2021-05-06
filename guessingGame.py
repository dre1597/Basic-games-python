import random

def welcome_message():
    print('*******************************')
    print('*Welcome to the guessing game!*')
    print('*******************************')

def get_secret_number():
    return round(random.randrange(1, 101))

def get_level():
    print('We have these levels')
    print('(1) Easy (2) Medium (3) Hard')

    level = int(input('What level do you wanna play?'))

    if level == 1:
        total_tries = 20
    elif level == 2:
        total_tries = 10
    else:
        total_tries = 5
    
    return total_tries

def guess_game(secret_number, total_tries):
    number_of_tries = 1
    points = 1000

    not_guessed = True
    not_lose = True

    while not_guessed and not_lose:

        print(f'Try {number_of_tries} of {total_tries}')
        guess = int(input('Give it a try: '))
        print('You tried', guess)

        if guess < 1 or guess > 100:
            print('Try again, but type a number between 1 and 100')
            continue

        guessed = secret_number == guess
        greater = secret_number > guess
        lesser = secret_number < guess

        if guessed:
            print(f'You are right! You got {points} points!')
            not_guessed = False
    
        else:
            if greater:
                print('You are wrong! The secret number is greater than this!')
            elif lesser:
                print('You are wrong! The secret number is lesser than this!')

            points_to_lose = abs(secret_number - guess)
            points = points - points_to_lose 
    
        number_of_tries = number_of_tries + 1
        if number_of_tries > total_tries:
            not_lose = False

def play():

    welcome_message()

    secret_number = get_secret_number()

    total_tries = get_level()

    print('We have a secret number! Take a guess! Type a number between 1 and 100')

    guess_game(secret_number, total_tries)

if __name__ == '__main__':
    play()





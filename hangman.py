import random


def welcome_message():
    print("*********************")
    print("*Welcome to hangman!*")
    print("*********************")


def get_secret_word():

    archive = open("words.txt", "r")
    words = []
    for line in archive:
        line = line.strip()
        words.append(line)

    random_number = random.randrange(0, len(words))
    secret_word = words[random_number].upper()

    archive.close()

    return secret_word


def get_mask(secret_word):
    return ["_" for letter in secret_word]


def get_guess():
    guess = input("What letter do you want? ")
    guess = guess.strip().upper()
    return guess


def verify_guess(secret_word, guess, mask):
    index = 0
    for letter in secret_word:
        if guess == letter:
            mask[index] = letter
        index += 1


def won_message(number_of_tries):
    print(f"You won in {number_of_tries} tries!")


def lose_message(secret_word):
    print(f"You lose! The secret word was {secret_word}")


def play():
    welcome_message()

    secret_word = get_secret_word()

    mask = get_mask(secret_word)
    print(mask)

    lose = False
    won = False
    errors = 0

    while not lose and not won:
        guess = get_guess()

        if guess in secret_word:
            verify_guess(secret_word, guess, mask)

        else:
            errors += 1
            if (6 - errors) == 0:
                print(f"That is your last try!")
            else:
                print(f"You are wrong! You have more {6 - errors} tries!")
        lose = errors == 6
        won = "_" not in mask

        print(mask)

        if won:
            won_message(6 - errors)
        if lose:
            lose_message(secret_word)


if __name__ == "__main__":
    play()

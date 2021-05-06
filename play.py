import guessingGame
import hangman

def choose_game():
    print('We have these games!')
    print('(1) Guessing game (2) Hangman')

    game = int(input('What game do you wanna play?'))

    if game == 1:
        print('Good luck on te guessing game!')
        guessingGame.play()

    elif game == 2:
        print('Good luck on hangman game!')
        hangman.play()

if __name__ == '__main__':
    choose_game()
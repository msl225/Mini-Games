
import random

list = ['r', 'p', 's']


def get_choice():
     while True:
        guess = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if guess not in list:
            print("invalid choice! pick from the options.")
            continue
        else:
            return guess

def show_results(guess, rando):
    print(f'You chose {guess}')
    print(f'Computer chose {rando}')

def det_win(guess, rando):
     if ((guess == "r" and rando == "s") or
         (guess == "p" and rando == "r") or
         (guess == "s" and rando == "p")):
        print("You won!")
     elif guess == rando:
         print("draw")
     else:
         print("You lose")


def play_game():
    while True:
        guess = get_choice()

        rando = random.choice(list)

        show_results(guess, rando)

        det_win(guess, rando)

        decide = input("Continue? (y/n): ").lower()
        if decide == "y":
            continue
        elif decide == "n":
            break
        else:
            print("invalid response")

play_game()




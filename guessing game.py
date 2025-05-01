import random


rando = random.randint(1, 100)

while True:
    try:
        choice = input("Guess a number between 1 an 100: ")
        intchoice = int(choice)
        if intchoice < rando:
            print("too low")
        elif intchoice > rando:
            print("too high")
        else:
            print(f'You got it! the number is {rando}')
            break
    except ValueError:
        print("Please enter a valid number.")

   
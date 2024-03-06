import random
import sys



def compare (a, b):
    if a > b:
        message = "Your guess is smaller than the answer" 
    elif b > a:
        message = "Your guess is larger than the answer"
    return message

def wrong(random_number, guess):
    guess = int(guess)
    clues = [
        f"You tried it! Your guess is {abs(random_number - guess)} away from the answer",

        f"You tried it! {compare(random_number, guess)}"
    ]

    print(random.choice(clues))
    


def game():
    random_number = random.randint(1, 100)

    print("I'm guessing a number from 1 to 100. Can you tell me which?")
    guess = input()
    if guess == "END":
        print("Come back again!")
        sys.exit()
    elif not guess.isdigit():
        print("Please enter a number")
        guess = input()
    elif len(guess.strip())== 0:
        print("Please enter a number to play the game")
        guess = input()

    while int(guess) != random_number:
        wrong(random_number, guess)
        print("Try again?")
        guess = input()
        if guess == "END":
            print("Come back again!")
            sys.exit()

    if int(guess) == random_number:
        print("Right on the money! Play again? Y/N")
        ans = input()
        if ans == "Y":
            random_number = random.randint(1, 100)
            game()
        elif ans == "N":
            print("Come back again!")
            sys.exit()



while True:
    prompt = input("Guess The Number Game \n Enter START to start game \n Enter END to end game: \n")

    if prompt == "END":
        print("Come back again!")
        sys.exit()
    elif prompt == "START":
        game()
    else:
        print("Enter one of the options and nothing else please")



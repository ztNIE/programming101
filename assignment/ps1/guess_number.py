# Guess the number between 0 and 100
from random import randint

if __name__ == "__main__":
    answer = randint(0, 100)

    while True:
        user_input = int(input("Please guess between 0 and 100: "))
        if user_input == answer:
            print("You are right!")
            break
        elif user_input < answer:
            print("Too small! Have another guess.")
        else:
            print("Too large! Have another guess.")

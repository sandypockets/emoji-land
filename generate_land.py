import random

from termcolor import colored
from noise import pnoise2


def generate_land(rows=10, cols=10):
    data = [" ", ".", "-", "#", "!", "$", "!", "#", "-", ".", " "]
    seed = random.randint(0, 100)
    land = ""

    print(f"Generate a landscape which is {cols} by {rows}")
    for row in range(rows):
        for col in range(cols):
            n = pnoise2(row / rows, col / cols, base=seed)
            n *= 100
            n = round(n)
            n = n % len(data)
            land += data[n]
        land += "\n"

    print(land)
    print("Finished generating landscape")
    return land


def ask_for_number(question):
    tries = 0
    while tries < 3:
        answer = input(colored(question, "green"))
        if answer == "quit":
            quit()
        elif answer.isnumeric():
            return int(answer)
        else:
            print(colored("Enter a number", "yellow"))
            tries += 1
    print(colored("Out of tries", "red"))
    quit()


if __name__ == "__main__":
    rows = ask_for_number("How many rows? ")
    cols = ask_for_number("How many columns? ")
    generate_land(rows, cols)

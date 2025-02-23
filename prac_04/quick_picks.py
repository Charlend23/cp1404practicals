import random
from random import randint

MIN_RANDOM = 1
MAX_RANDOM = 45
COLUMN_EACH_ROW = 6

def main():
    user_picks = int(input("How many quick picks? "))
    for i in range(user_picks):
        picks = generate_picks()
        print(" ".join(f"{number:2}" for number in picks))


def generate_picks():
    random_number = []
    while len(random_number) < COLUMN_EACH_ROW:
        numbers = randint(MIN_RANDOM,MAX_RANDOM)
        if numbers not in random_number:
         random_number.append(numbers)
    return sorted(random_number)

main()
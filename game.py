import random

for c in [99]*10+[49]*10:
    a, b = random.randint(1, c), 0
    while a != b:
        b = int(input(f"Enter an integer from 1 to {c}: "))
        print("guess is low" if b < a else "guess is high" if b > a else "you guessed it!")

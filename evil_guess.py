import random

random_number = random.randrange(1, 11)
count = 0
while count<1:
    guess = input("guess a number 1-10: ")
    if int(guess) == random_number:
        print("good job, you win.... the number was", random_number)
    else:
        print("..... no hint for you, keep guessing until you get it right")
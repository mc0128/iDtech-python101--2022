import random
random_number = (random.randint(1, 50))
bomb = (random.randint(1, 50))
while bomb == random_number:
    bomb = (random.randint(1, 50))
guessed = False
lives = 5
while not guessed and lives > 0:
    guess = int(input("pick a number"))
    if guess == bomb:
        print("You have activated the bomb.")
        lives = 0
    elif guess == random_number:
        guessed = True
        print("You have guessed correctly")
    elif guess < random_number:
        print("Your guess is too low.")
        lives = lives - 1
    elif guess > random_number:
        print("Your guess is too high.")
        lives = lives - 1
if lives == 0:
    print("You lost. You ran out of lives")
else:
    print("You won!")

import random

print("Hello, What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 0 and 20")
secret_Num = random.randint(1, 20)  # generate a random number between 0 and 20 (including 20)

for guessTaken in range(1, 7):  # 6 guesses
    print("Take a guess.")
    guess = int(input())

    if guess < secret_Num:
        print("Your guess is too low.")
    elif guess > secret_Num:
        print("Your guess is too high.")
    else:
        break   # break out of loop for the correct guess

if guess == secret_Num:
    print("Bingo! You guessed the number in " + str(guessTaken) + " guesses!")
else:
    print("Nope, the number I was thinking of was " + str(secret_Num))

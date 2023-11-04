import random

secret_word = "mosiah"
guess_count = 3

print("Welcome to the word guessing game!")

while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guess{'es' if guess_count > 1 else ''}.")
        break
    else:
        print("Your guess was not correct.")
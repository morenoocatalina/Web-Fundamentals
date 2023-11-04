quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

run_again = "yes"

while run_again == "yes":
    secret_word = quote.lower()  
    user_guess = ""

   
    num_guesses = 0

   
    hint = "_" * len(secret_word)

    print("\nWelcome to the word guessing game!")
    
    while hint != secret_word:
        print("\nYour hint is:", hint)
        user_guess = input("What is your guess? ").lower()
        num_guesses += 1

        if len(user_guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            continue

        for i, letter in enumerate(secret_word):
            if user_guess[i] == letter:
                hint = hint[:i] + user_guess[i] + hint[i + 1:]

        if hint == secret_word:
            break

    print("\nCongratulations! You guessed it!")
    print("It took you", num_guesses, "guesses.")

    run_again = input("Would you like to play again? ")

print("Goodbye")


import random

words = ["apple", "banana", "mango", "cherry", "grapes"]
secret = random.choice(words)

display = []
for i in secret:
    display.append("_")

wrong = 0
used_letters = []

print("Welcome to Hangman Game!")
print("Guess the word. It has", len(secret), "letters.")
print("You can make 6 wrong guesses.\n")

while wrong < 6 and "_" in display:
    print("Word:", " ".join(display))
    print("Used letters:", " ".join(used_letters))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Only single letters are allowed.\n")
        continue

    if guess in used_letters:
        print("You've already tried that letter.\n")
        continue

    used_letters.append(guess)

    if guess in secret:
        print("Nice! That letter is in the word.\n")
        for i in range(len(secret)):
            if secret[i] == guess:
                display[i] = guess
    else:
        print("Oops! Wrong guess.\n")
        wrong += 1

if "_" not in display:
    print("You won! The word was:", secret)
else:
    print("You lost! The word was:", secret)
print("Made by Shubham!")

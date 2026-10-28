
import random

words = ["python", "laptop", "college", "coding", "program"]
word = random.choice(words)
guessed = []
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if all(letter in guessed for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess one letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one letter only.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
    elif guess in word:
        guessed.append(guess)
        print("Correct guess!")
    else:
        guessed.append(guess)
        attempts -= 1
        print("Wrong guess!")

if attempts == 0:
    print("Game over! The word was:", word)

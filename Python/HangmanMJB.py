import random

def get_random_word():
    words = [
        "mark", "eyebrow", "abridge", "contact", "secretary", "effective",
        "charm", "inside", "start", "attitude", "suppress", "manner", "ball",
        "empire", "bet", "aunt", "inquiry", "candle", "cooperate", "continuous"
    ]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    while attempts > 0:
        print(f"Word: {display_word(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congrats! You guessed the word: {word}")
                return
        else:
            guessed_letters.add(guess)
            attempts = attempts - 1
            print(f"Incorrect! {attempts} attempts left.")
            if attempts == 5:
                print(
                    "----------|   ", "\n",
                    "         O    ", "\n",)
            if attempts == 4:
                print(
                    "----------|   ", "\n",
                    "         O    ", "\n",
                    "         |    ", "\n",)
            if attempts == 3:
                print(
                    "----------|   ", "\n",
                    "         O    ", "\n",
                    "        /|    ", "\n",)
            if attempts == 2:
                print(
                    "----------|   ", "\n",
                    "         O    ", "\n",
                    "        /|\   ", "\n",)
            if attempts == 1:
                print(
                    "----------|   ", "\n",
                    "         O    ", "\n",
                    "        /|\   ", "\n",
                    "        /     ", "\n",)

    print("Game over! The word was: ", word, "\n",
        "----------|   ", "\n",
        "         O    ", "\n",
        "        /|\   ", "\n",
        "        / \  ", "\n",
        "You have been hanged!")

hangman()
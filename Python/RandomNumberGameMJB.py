import random

randomnumber = random.randint(1, 100)
tries = 0
playing = "yes"

print("Welcome to the Random Number Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess the number.")
while playing == "yes":
    randomnumber = random.randint(1, 100)
    guess = None  
    tries = 0
    while guess != randomnumber:
        guess = int(input("Enter your guess: "))
        tries += 1
        if guess < randomnumber:
            print("Higher!")
        elif guess > randomnumber:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {tries} tries.")
    print("Would you like to play again?")
    playing = input("Enter yes or no: ")

import random

def generate_lottery_numbers():
    winning_numbers = set()
    while len(winning_numbers) < 5:
        winning_numbers.add(random.randint(1, 70))
    winning_powerball = random.randint(1, 25)
    return list(winning_numbers) + [winning_powerball]

def get_user_numbers():
    user_numbers = set()
    while len(user_numbers) < 5:
        try:
            num = int(input(f"Enter your number (1-70): "))
            if 1 <= num <= 70 and num not in user_numbers:
                user_numbers.add(num)
            else:
                print("Invalid or duplicate number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 70.")
    
    while True:
        try:
            user_powerball = int(input("Enter your Powerball number (1-25): "))
            if 1 <= user_powerball <= 25:
                break
            else:
                print("Invalid number. Enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 25.")
    
    return list(user_numbers) + [user_powerball]

def get_quick_numbers():
    quick_numbers = set()
    while len(quick_numbers) < 5:
        num = random.randint(1, 70)
        if num not in quick_numbers:
            quick_numbers.add(num)
    quick_powerball = random.randint(1, 25)
    return list(quick_numbers) + [quick_powerball]

def main():
    print("Welcome to the Lottery!")

    lottery_numbers = generate_lottery_numbers()

    print("Would you like to enter your own numbers or get quick pick numbers?")
    print("Enter 1 for your own numbers or 2 for quick pick numbers.")
    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                user_numbers = get_user_numbers()
                break
            elif choice == 2:
                user_numbers = get_quick_numbers()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    print(f"Your numbers are: {user_numbers}")
    print(f"The winning numbers are: {lottery_numbers}")

    matches = set(lottery_numbers[:5]) & set(user_numbers[:5])
    powerball_match = lottery_numbers[5] == user_numbers[5]

    print(f"You matched {len(matches)} regular numbers and {'the Powerball' if powerball_match else 'no Powerball'}.")


main()
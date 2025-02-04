# Initialize the board spots
spot1 = "1"
spot2 = "2"
spot3 = "3"
spot4 = "4"
spot5 = "5"
spot6 = "6"
spot7 = "7"
spot8 = "8"
spot9 = "9"

def display_board():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
    print(' ', spot1, ' | ', spot2, ' | ', spot3, ' ')
    print("----------------")
    print(' ', spot4, ' | ', spot5, ' | ', spot6, ' ')
    print("----------------")
    print(' ', spot7, ' | ', spot8, ' | ', spot9, ' ')
    print("\n")

def pick_spot():
    while True:
        try:
            spot = int(input("Pick a spot: "))
            return spot
        except ValueError:
            print("Invalid input, please enter a number.")

def place_spotX():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
    spot = int(pick_spot())
    if spot == 1:
        spot1 = "X"
    elif spot == 2:
        spot2 = "X"
    elif spot == 3:
        spot3 = "X"
    elif spot == 4:
        spot4 = "X"
    elif spot == 5:
        spot5 = "X"
    elif spot == 6:
        spot6 = "X"
    elif spot == 7:
        spot7 = "X"
    elif spot == 8:
        spot8 = "X"
    elif spot == 9:
        spot9 = "X"
    else:
        print("Invalid spot, try again.")
        place_spotX()

def place_spotO():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
    spot = int(pick_spot())
    if spot == 1:
        spot1 = "O"
    elif spot == 2:
        spot2 = "O"
    elif spot == 3:
        spot3 = "O"
    elif spot == 4:
        spot4 = "O"
    elif spot == 5:
        spot5 = "O"
    elif spot == 6:
        spot6 = "O"
    elif spot == 7:
        spot7 = "O"
    elif spot == 8:
        spot8 = "O"
    elif spot == 9:
        spot9 = "O"
    else:
        print("Invalid spot, try again.")
        place_spotO()

def check_spot(spot):
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
    if spot == 1:
        return spot1
    elif spot == 2:
        return spot2
    elif spot == 3:
        return spot3
    elif spot == 4:
        return spot4
    elif spot == 5:
        return spot5
    elif spot == 6:
        return spot6
    elif spot == 7:
        return spot7
    elif spot == 8:
        return spot8
    elif spot == 9:
        return spot9

def check_spot_taken(spot):
    if check_spot(spot) in ["X", "O"]:
        print("Spot already taken, try again.")
        return True
    return False

def check_win():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
    if (spot1 == spot2 == spot3) or (spot4 == spot5 == spot6) or (spot7 == spot8 == spot9) or \
       (spot1 == spot4 == spot7) or (spot2 == spot5 == spot8) or (spot3 == spot6 == spot9) or \
       (spot1 == spot5 == spot9) or (spot3 == spot5 == spot7):
        return True
    return False

def main():
    display_board()
    for turn in range(9):
        if turn % 2 == 0:
            print("Player X's turn")
            place_spotX()
        else:
            print("Player O's turn")
            place_spotO()
        
        display_board()
        
        if check_win():
            if turn % 2 == 0:
                print("Player X wins!")
            else:
                print("Player O wins!")

        
    print("It's a tie!")

main()
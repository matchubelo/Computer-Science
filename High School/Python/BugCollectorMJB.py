days = 0
totalbugs = 0

while days < 7:
    daybugs = int(input("How many bugs did you collect? "))
    totalbugs = daybugs + totalbugs
    days = days + 1

print("The total number of bugs collected is: ", totalbugs)
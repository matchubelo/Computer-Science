day = 1
totalsales = 0

while day <= 7:
    daysales = float(input("How much money did you make today? "))
    totalsales = totalsales + daysales
    day += 1

print("Your weekly sale total is: $", format(totalsales, '.2f'))
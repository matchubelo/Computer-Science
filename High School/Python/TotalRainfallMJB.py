# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, the average monthly
# rainfall, and the months with the highest and lowest amounts.

month = 1
rainfall_data = []
while month <= 12:
    while True:
        try:
            rainfall = float(input(f"Enter the total rainfall for month {month}: "))
            if rainfall < 0:
                print("Rainfall cannot be negative. Please enter a valid amount.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    rainfall_data.append(rainfall)
    month = month + 1

total_rainfall = sum(rainfall_data)
average_rainfall = total_rainfall / 12
highest_rainfall = max(rainfall_data)
lowest_rainfall = min(rainfall_data)

print("The rainfall entered for the year is: ", "\n", rainfall_data)
print("The total rainfall for the year is: ", format(total_rainfall, '.2f'), " inches")
print("The average monthly rainfall is: ", format(average_rainfall, '.2f'), " inches")
print("The highest month had: ", format(highest_rainfall, '.2f'), " inches of rain")
print("The lowest month had: ", format(lowest_rainfall, '.2f'), " inches of rain")

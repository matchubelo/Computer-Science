day = 1
sales = []

while day <= 7:
    daysales = float(input("How much money did you make today? "))
    sales.append(daysales)
    day += 1

print("Your weekly sale total is: $", format(sum(sales), '.2f'))
print("Your daily sales are: ", "\n", sales)
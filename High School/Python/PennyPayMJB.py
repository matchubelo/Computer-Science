days=int(input("Enter the number of days: "))

count = 0
pay = 0 
penny = 1

while count < days:
    pay = pay + penny
    penny = penny * 2
    count = count + 1
    print("Day", count, "Salary: $", format(penny/100, ".2f"))
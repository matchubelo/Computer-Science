userinput = int(input("Enter a positive numbers, the program will continue until a negative number is entered: "))
total_sum = 0
while userinput >= 0:
    total_sum = userinput + total_sum
    userinput = int(input("Enter a positive numbers, the program will continue until a negative number is entered: "))
print("The sum of the numbers is:", total_sum)
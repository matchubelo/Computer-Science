celsius = 0
for celsius in range(21):
    fahrenheit = (9/5) * celsius + 32
    print(celsius, "Celsius is equal to", format(fahrenheit, ".2f"), "Fahrenheit")
    celsius = celsius + 1
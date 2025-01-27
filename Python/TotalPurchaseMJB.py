I1 = input("What is the price of the first item? ")
print("")

I2 = input("What is the price of the second item? ")
print("")

I3 = input("What is the price of the third item? ")
print("")

I4 = input("What is the price of the fourth item? ")
print("")

I5 = input("What is the price of the fifth item? ")
print("")

Subtotal = float(I1) + float(I2) + float(I3) + float(I4) + float(I5)
SalesTax = (float(I1) + float(I2) + float(I3) + float(I4) + float(I5)) * 0.0635
Total = Subtotal + SalesTax

print("Prices:\n", 
      "$" + format(float(I1), '.2f'), "\n", 
      "$" + format(float(I2), '.2f'), "\n", 
      "$" + format(float(I3), '.2f'), "\n", 
      "$" + format(float(I4), '.2f'), "\n", 
      "$" + format(float(I5), '.2f'), "\n",
      "", "\n",
      "Subtotal: $", format((Subtotal), '.2f'), "\n", 
      "Sales Tax: $", format((SalesTax), '.2f'), "\n", 
      "Total: $", format((Total), '.2f'))
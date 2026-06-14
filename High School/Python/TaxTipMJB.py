Subtotal = input("Enter the subtotal: ")
print("")

Tip = input("Enter the tip percentage: ")

Tax = float(Subtotal) * float(0.0635)

TipAmount = float(Subtotal) * (float(Tip) / 100)

Total = float(Subtotal) + float(Tax) + float(TipAmount)

print("Subtotal: $", format(float(Subtotal), '.2f'), "\n",
        "Tax: $", format(float(Tax), '.2f'), "\n",
        "Tip: $", format(float(TipAmount), '.2f'), "\n",
        "Total: $", format(float(Total), '.2f'))
def GetSQFT():
    SQFT = float(input("Enter the square footage of the wall space to be painted: "))
    return SQFT

def GetPrice(SQFT):
    Gallons = float(SQFT // 115)
    GallonPrice = float(Gallons * 60)
    Hours = float(Gallons * 8)
    LaborPrice = float(Hours * 20)
    TotalPrice = float(GallonPrice + LaborPrice)
    return Gallons, GallonPrice, Hours, LaborPrice, TotalPrice


SQFT =  GetSQFT()
Gallons, GallonPrice, Hours, LaborPrice, TotalPrice = GetPrice(SQFT)
print("For ", format(SQFT, '.1f'), "Sqaure Feet", "\n",
    "You will need ", format(Gallons, '.2f'), "gallons of paint", "\n",
    "The price of the paint is $", format(GallonPrice, '.2f'), "\n",
    "The labor cost is $", format(LaborPrice, '.2f'), "for", format(Hours, '.1f'), "hours", "\n",
    "\n",
    "The total cost is $", format(TotalPrice, '.2f'))

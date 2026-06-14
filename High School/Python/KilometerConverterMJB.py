def GetKM():
    Kilometers = input("Enter the number of kilometers: ")
    return Kilometers

def CalculateMiles(Kilometers):
    Miles = float(Kilometers) * 0.6214
    return Miles

Kilometers = GetKM()
Miles = CalculateMiles(Kilometers)
print("The number of miles for ", Kilometers, "km ", "is: ", format(float(Miles), '.1f'), "miles")
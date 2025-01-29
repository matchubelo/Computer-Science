def GetA():
    A = int(input("Enter the number of class A tickets sold: "))
    return A

def GetB():
    B = int(input("Enter the number of class B tickets sold: "))
    return B

def GetC():
    C = int(input("Enter the number of class C tickets sold: "))
    return C

def CalculateRevenue(A, B, C):
    A_Revenue = float(A * 15)
    B_Revenue = float(B * 12)
    C_Revenue = float(C * 9)
    TotalRevenue = float(A_Revenue) + float(B_Revenue) + float(C_Revenue)
    return A_Revenue, B_Revenue, C_Revenue, TotalRevenue

A = GetA()
B = GetB()
C = GetC()

A_Revenue, B_Revenue, C_Revenue, TotalRevenue = CalculateRevenue(A, B, C)
print("Revenue Broken Down: \n",
    "Revenue generated from class A tickets: $", format(A_Revenue, '.2f'), "\n",
    "Revenue generated from class B tickets: $", format(B_Revenue, '.2f'), "\n",
    "Revenue generated from class C tickets: $", format(C_Revenue, '.2f'), "\n",
    "Total revenue generated: $", format(TotalRevenue, '.2f'))
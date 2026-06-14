def GetHours():
    Hours = float(input("Enter the amount of Hours: "))
    return Hours

def GetRate():
    Rate = float(input("Enter the Rate: "))
    return Rate

def CalculateOvertime(Hours, Rate):
    if Hours > 40:
        OvertimeHours = Hours - 40
        OvertimeRate = Rate * 1.5
        OvertimePay = OvertimeHours * OvertimeRate
        RegularPay = 40 * Rate
        TotalPay = OvertimePay + RegularPay
    else:
        TotalPay = Hours * Rate
    return TotalPay

Hours = GetHours()
Rate = GetRate()
TotalPay = CalculateOvertime(Hours, Rate)
print("Total pay is: ", TotalPay)
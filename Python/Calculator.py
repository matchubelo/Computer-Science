N1 = input("Enter a number: ")
print("")

N2 = input("Enter the another number: ")
print("")

Func = input("Enter the operation you want to perform: ")

if Func == "+":
    print(N1, "+", N2, "=", float(N1) + float(N2))
elif Func == "-":
    print(N1, "-", N2, "=", float(N1) - float(N2))
elif Func == "*" or Func == "x":
    print(N1, "*", N2, "=", float(N1) * float(N2))
elif Func == "/":
    print(N1, "/", N2, "=", float(N1) / float(N2))
else: 
    print("Invalid operation.")
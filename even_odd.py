try:
    inputNumber = int(input("Enter number : "))
    numberType = "EVEN" if inputNumber % 2 == 0 else "ODD"
    print(f"{inputNumber} is an {numberType} number")
except ValueError:
    print("Input is ngot a number")
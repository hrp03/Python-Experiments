try:
    inputNumber = int(input("Enter number : "))
    a, factorial = [1, 1]
    while a <= inputNumber:
        factorial *= a
        a += 1
    print(f"{inputNumber}! = {factorial}")
except ValueError:
    print("Input number is not a number")
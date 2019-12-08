try:
    lastNumber = int(input("Enter last number : "))
    a, b, c = [0, 1, 1]
    fibonacciSeries = f"{a} {b}"
    while c < lastNumber:
        fibonacciSeries += " " + str(c)
        c = a + b
        a = b
        b = c
        
    print(fibonacciSeries)
except ValueError:
    print("Input number is not a number")
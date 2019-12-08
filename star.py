try:
    starHeight = int(input("Enter height of star : "))
    i = 1
    while i <= starHeight:
        print("*" * i)
        i += 1
except ValueError:
    print("Input is not a number")


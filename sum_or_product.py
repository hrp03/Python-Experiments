# Write a program that asks the user for a number n and gives them the 
# possibility to choose between computing the sum and computing the product of 1,…,n.

def getSum(number):
    return (number * (number + 1)) / 2

def getProduct(number):
    product = 1
    for i in range(1, number+1):
        product *= i
    return product

try:
    input_number = int(input("Enter number : "))
    choice = input("Compute sum or product : ")
    print(choice)
    if choice == "sum":
        print(f"Sum of number till n is {getSum(input_number)}")
    elif choice == "product":
        print(f"Product of number till n is {getProduct(input_number)}")

except:
    print("Enter correct input")
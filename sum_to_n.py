# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

try:
    number = int(input("Enter a number : "));
    sum = (number * (number + 1))/2;
    print(f"Sum of number 1 ... {number} is {sum}");

except:
    print("Enter number only")

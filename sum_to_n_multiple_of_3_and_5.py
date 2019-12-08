# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
# such that only multiples of three or five are considered in the sum, 
# e.g. 3, 5, 6, 9, 10, 12, 15 for n = 17

def getSumOf3and5Method1(input_number):
    i3 = int(input_number/3)
    i5 = int(input_number/5)
    i15 = int(input_number/15)

    return (3 * ((i3 * (i3+1)) / 2)) + (5 * ((i5 * (i5+1)) / 2)) - (15 * ((i15 * (i15+1)) / 2))

def getSumOf3and5Method2(input_number):
    sum = 0
    for number in range(1, input_number + 1):        
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum

try:
    input_number = int(input("Enter a number : "))
    sum_method_1 = getSumOf3and5Method1(input_number)
    sum_method_2 = getSumOf3and5Method2(input_number)
    print(f"Method 1 Sum : {int(sum_method_1)}")
    print(f"Method 2 Sum : {sum_method_2}")
except:
    print("Enter correct input")
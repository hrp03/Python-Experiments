# Write a function that computes the running total of a list.

try:

    list_of_numbers = []
    total = 0

    while True:
        input_number = int(input("Enter a number to add or zero to stop : "))
        if(input_number == 0):
            break
            
        list_of_numbers.append(input_number)    
        total += input_number 
        print(list_of_numbers)
        print(f"Running total : { total }")

        

except:
    print("Enter number only")
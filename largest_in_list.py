# Write a function that returns the largest element in a list.

def getLargest(list_of_numbers):
    max = 0
    for number in list_of_numbers:
        if number > max:
            max = number
    return max

list_of_numbers = [3,2,4,5,6,12,78,65,34,21,144,99,8,67,66,87]

print(f"Largest number is in list is : {getLargest(list_of_numbers)}")

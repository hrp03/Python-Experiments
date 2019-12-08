#Write a function that checks whether an element occurs in a list.

def checkIfExists(list_of_number, to_check):
    for i in range(len(list_of_numbers)):
        if list_of_number[i] == to_check:
            return f"{to_check} is available in list at index {i}"
    return f"{to_check} is not present in list"

  
list_of_numbers = [3,2,4,5,6,12,78,65,34,21,144,99,8,67,66,87,100]

print(checkIfExists(list_of_numbers, 120))

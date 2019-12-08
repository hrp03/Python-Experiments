# Write a function that returns the elements on odd positions in a list.

def getFromOddPosition(list_of_number):
    odd_position_array = []
    for i in range(1, len(list_of_numbers), 2):
        odd_position_array.append(list_of_number[i])
        
    return odd_position_array

  
list_of_numbers = [3,2,4,5,6,12,78,65,34,21,144,99,8,67,66,87,100]

print(getFromOddPosition(list_of_numbers))
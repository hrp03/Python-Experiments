# Write function that reverses a list, preferably in place.

def getReverseList(list_of_numbers):

    length = len(list_of_numbers) - 1
    last = int(length / 2) + 1

    for i in range(last):
        print(f"{i}-{length-i}")
        temp = list_of_numbers[i]
        list_of_numbers[i] = list_of_numbers[length - i]
        list_of_numbers[length - i] = temp

    return list_of_numbers

list_of_numbers = [3,2,4,5,6,12,78,65,34,21,144,99,8,67,66,87,100]

reversed_list = getReverseList(list_of_numbers)
print(reversed_list)


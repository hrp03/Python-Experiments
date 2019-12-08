# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was
# too large or too small. At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.

import random

try:
    print("Guess number between 1 and 10")
    try_count = 0

    while try_count < 3:
        new_number = random.randint(1,10)
        input_number = int(input("Your Guess : "))
        if new_number == input_number:
            print("Correct, You Win!")
            break
        else:
            try_count += 1
            print(f"Oops the number is {new_number} \n {3 - try_count} chances remaining")
except TypeError:
    print("Enter number only")

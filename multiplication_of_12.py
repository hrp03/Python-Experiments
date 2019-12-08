# Write a program that prints a multiplication table for numbers up to 12.

numbers = 13

for i in range(1, numbers):
    for j in range(1, numbers):
        print(f"{i*j}", end="\t")
    print("")

# Write a program that prints all prime numbers.
# (Note: if your programming language does not support arbitrary size numbers, 
# printing all primes up to the largest number you can easily represent is fine too.)

for i in range(2, 1000):

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=",")

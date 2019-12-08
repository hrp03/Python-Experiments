# Write three functions that compute the sum of the numbers in a list: using a for-loop,
# a while-loop and recursion. (Subject to availability of these constructs in your
# language of choice.)

def sumWhileLoop(list):
    sum = 0
    i = 0
    while i < len(list):
        sum += list[i]
        i += 1
    return sum

def sumForLoop(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

def sumRecursion(list):
    if len(list) == 0:
        return 0
    else :
        return list[0] + sumRecursion(list[1:])

list = [1,2,12,32]

print(f"While Loop Sum : {sumWhileLoop(list)}")
print(f"For Loop Sum : {sumForLoop(list)}")
print(f"Recursion Sum : {sumRecursion(list)}")
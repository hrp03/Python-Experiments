# Write a function that tests whether a string is a palindrome.

def method1(string):
    return string[::-1] == string

def method2(string):
    newstring = ""
    length = len(string)
    for i in range(length):
        newstring += string[length - i - 1]
    return newstring == string

string = input("Enter a string : ")

if method1(string):
    print("Method 1 : Palindrome")
else :
    print("Method 1 : Not Palindrome")

if method2(string):
    print("Method 2 : Palindrome")
else :
    print("Method 2 : Not Palindrome")
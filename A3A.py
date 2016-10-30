#Name: Jeffrey Shen
#Student ID: 10153021
#Program asks user for character(s), then concatenates randomly generated integer between 1-100 with character(s)
#The program prints out the output as a string

import random

print("Enter character(s) to receive your secret composite code")
randomNumber = str(random.randrange(1,100))
#parameter n: number generated from random.randrange
def completeCode(n):
    word = input("Enter character part of code:")
    result = n + word
    print("Your secret composite code is:", result)

completeCode(randomNumber)

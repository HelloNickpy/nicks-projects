import random

print("""Password Generator   
--------          """.upper())

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&0123456789"

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Input password length: ")
length = int(length)

print("\nHere are your passwords: ")

for i in range(number):
    passwords = ''
    for x in range(length):
        passwords += random.choice(chars)
    print(passwords)

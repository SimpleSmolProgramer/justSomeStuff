import random

print("Welcome to the random password generator")

print()

print("Please choose from these options: ")
print("1.  Numbers 123")
print("2.  Special !@#$%^&*")
print("3.  Letter abc")
print("4.  Letter + Special")
print("5.  Letter + Number")
print("6.  Letter + Number + Special")

choice = int(input(">> "))

print()

print("Please enter the length of your password.")

length = int(input(">> "))

special = "!@#$%^&*áƒÆ£æè®êÛ"
letter = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

password = ""

if choice == 1:
    for i in range(length):
        password += random.choice(numbers)

elif choice == 2:
    for i in range(length):
        password += random.choice(special)

elif choice == 3:
    for i in range(length):
        password += random.choice(letter)

elif choice == 4:
    for i in range(length):
        password += random.choice(special + letter)

elif choice == 5:
    for i in range(length):
        password += random.choice(numbers + letter)

elif choice == 6:
    for i in range(length):
        password += random.choice(special + letter + numbers)

print()

print("Here is your password →  {}  ← Thank you! ".format(password))

print()

end = input("PRESS ENTER TO CLOSE...")
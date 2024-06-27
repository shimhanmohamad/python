import random
import string
print("Welcome to PyPassword genarator")
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
           'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!','@','#','$','&','(',')','*','+']

letter_u  = int(input("How many letters do you w3ant to in your password ? \n"))
number_u = int(input("How many numbers do you want to in your password ? \n"))
symbol_u= int(input("How many symbols do you want to in your password ? \n"))

password = []

# choose_letters = random.choice(letters)
# choose_numbers = random.choice(numbers)
# choose_symbols = random.choice(symbols)

for char in range(1,letter_u + 1):
    password.append(random.choice(letters))
for inte in range(1,number_u + 1):
    password.append(random.choice(numbers))
for sym in range(1,symbol_u + 1):
    password.append(random.choice(symbols))

random.shuffle(password)
password_list = ""
for char in password:
    password_list += char

print(f"Your password : {password_list}")


import random
import string
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
           'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!','@','#','$','&','(',')','*','+']
print("Welcome to the Pypassword Generator")
nr_letters = int(input("how amny letters would you like in your password ? \n"))
nr_symbols = int(input(f"How many symbols would you like ? \n"))
nr_numbers = int(input(f"How many numberwould you like ? \n"))

# password = ""

# for char in range(1,nr_letters + 1):
#     password = password + random.choice(letters)
# for symbol in range(1,nr_symbols + 1):
#     password = password + random.choice(symbols)
# for number in range(1,nr_numbers + 1):
#     password = password + random.choice(numbers)

# print(password)
# shuffle_password =random.shuffle(password)
# print(shuffle_password)
password = []

for char in range(1,nr_letters + 1):
    password.append(random.choice(letters))
for symbol in range(1,nr_symbols + 1):
    password.append(random.choice(symbols))
for number in range(1,nr_numbers + 1):
    password.append(random.choice(numbers))


random.shuffle(password)


password_list = ""
for char in password:
    password_list += char
print(f"your password is  :  6{password_list}")



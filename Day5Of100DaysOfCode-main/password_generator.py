import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pass_app = input("Which app would you like to generate a password for?: ").upper()
print(f"Let's generate a password for: {pass_app}")

num_letters = int(input("How many letters would you like to include in your password?: "))
num_numbers = int(input("How many numbers would you like in your password?: "))
num_symbols = int(input("How many symbols would you like included in your password?: "))

app_password = " "

for letter in range(1, num_letters + 1):
    random_letter = random.choice(letters)
    app_password += random_letter
    
for num in range(1, num_numbers + 1):
    random_number = random.choice(numbers)
    app_password += random_number
    
for symbol in range(1, num_symbols + 1):
    random_symbol = random.choice(symbols)
    app_password += random_symbol
 
print('Password generation complete!')   
print(f"Your passwrd for {pass_app} is {app_password}")
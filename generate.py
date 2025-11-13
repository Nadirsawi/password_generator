import random
import time

# Length: min: 8 characters
# *************
# *** Rules ***
# *************
# TODO: # 1. At least one uppercase letter
# TODO: # 2. At least one lowercase letter
# TODO: # 3. At least one digit
# TODO: # 4. At least one symbol

password: str = ""

uppercase_letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters: str = "abcdefghijklmnopqrstuvwxyz"
digits: str = "0123456789"
symbols: str = r'!@#$%^&*()-_=+[]\{}|;:\'",.<>?/`~'


# Generate password function
def generate_password():
    while True:
        try:
            password_length = int(
                input("Enter desired password length more than 8: ").strip()
            )
            if int(password_length) >= 8:
                # Call uppercase letter function
                uppercase = add_uppercase(
                    uppercase=uppercase_letters, length=password_length
                )
                # Call lowercase letter function
                lowercase = add_lowercase(
                    lowercase=lowercase_letters, length=password_length
                )
                # Call digit function
                digit = add_digits(digit=digits, length=password_length)
                # Call symbol function
                symbol = add_symbols(symbol=symbols, length=password_length)
                # Generate password
                # TODO : Add a timer
                timer: int = 3
                while timer != 0:
                    print("Generating password...")
                    time.sleep(1)
                    timer -= 1
                # Generate final password
                password = uppercase + lowercase + digit + symbol
                # Shuffle the password
                password = shuffle_password(password=password)
                print(f"Generated Password: {password}")
                break
            else:
                print("Please enter a number more than or equal to 8.")
                continue
        except:
            print("Invalid input. Please enter a number more than or equal to 8.")
            continue


# Uppercase letter function
def add_uppercase(uppercase: str, length: int):
    random_letters: str = ""
    for i in range(length // 4):
        random_letters += random.choice(uppercase)
    return random_letters


# Lowercase letter function
def add_lowercase(lowercase: str, length: int):
    random_letters: str = ""
    for i in range(length // 4):
        random_letters += random.choice(lowercase_letters)
    return random_letters


# Digit function
def add_digits(digit: str, length: int):
    random_digit: str = ""
    for i in range(length // 4):
        random_digit += random.choice(digit)
    return random_digit


# Symbol function
def add_symbols(symbol: str, length: int):
    random_symbol: str = ""
    for i in range(length // 4):
        random_symbol += random.choice(symbol)
    return random_symbol


# Shuffle password function
def shuffle_password(password: str):
    shuffled_password: str = ""
    lst = list(password)
    random.shuffle(lst)
    for i in lst:
        shuffled_password += i
    return "".join(shuffled_password)


if __name__ == "__main__":
    generate_password()

import random
import string

chars = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = chars.copy()
random.shuffle(key)


def generate_password():
    """Gera uma senha aleatória com o número de caracteres especificado."""
    try:
        num_characters = int(input("How many characters do you want in your new password:\n>>> "))
        if num_characters <= 0:
            print("Number must be greater than zero.")
            return
        new_password = ''.join(random.choice(chars) for _ in range(num_characters))
        print(f"\nHere is your new password: {new_password}")
    except ValueError:
        print("Please enter a valid number.")


def encrypt_message():
    """Criptografa uma mensagem usando um mapeamento simples entre 'chars' e 'key'."""
    message = input("Type your message to encrypt:\n>>> ")
    encrypted = ""
    for letter in message:
        encrypted += key[chars.index(letter)] if letter in chars else letter
    print(f"Encrypted message: {encrypted}")


def decrypt_message():
    """Descriptografa uma mensagem previamente criptografada."""
    message = input("Type your encrypted message:\n>>> ")
    decrypted = ""
    for letter in message:
        decrypted += chars[key.index(letter)] if letter in key else letter
    print(f"Decrypted message: {decrypted}")
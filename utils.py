import random
import string
from cryptography.fernet import Fernet

chars = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = chars.copy()
random.shuffle(key)

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)


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
    """Criptografa uma mensagem usando Fernet"""
    message = input("Type your message to encrypt:\n>>> ")
    encrypted_value = cipher_suite.encrypt(message.encode())  # o encode converte string para bytes
    print(f"Encrypted message: {encrypted_value.decode()}")


def decrypt_message():
    """Descriptografa uma mensagem criptografada anteriormente."""
    encrypted_input = input("Type your encrypted message:\n>>> ")
    try:
        decrypted_bytes = cipher_suite.decrypt(encrypted_input.encode())
        print(f"Decrypted message: {decrypted_bytes.decode()}")
    except Exception as e:
        print("Failed to decrypt. Make sure the message is valid and was encrypted with this key.")
        print(f"Error: {e}")
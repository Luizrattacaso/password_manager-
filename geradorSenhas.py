import random
import string

chars = list(" " + string.punctuation + string.digits + string.ascii_letters)

aux = chars.copy()
random.shuffle(aux)
key = aux

def menu(chars, key):
    while True:
        print()
        print("-=" * 30)
        print("MENU".center(60))
        print("-=" * 30)
        print("[1] Create a new password.")
        print("[2] Encrypt a message.")
        print("[3] Decrypt a message.")
        print("[4] Exit\n")

        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match option:
            case 1:
                try:
                    num_characters = int(input("How many characters do you want in your new password? "))
                    new_password = ''.join(random.choice(chars) for _ in range(num_characters))
                    print(f"\nHere is your new password: {new_password}")
                except ValueError:
                    print("Please enter a valid number.")

            case 2:
                message = input("Type your message to encrypt: ")
                encrypted_message = ""
                for letter in message:
                    if letter in chars:
                        index = chars.index(letter)
                        encrypted_message += key[index]
                    else:
                        encrypted_message += letter
                print(f"Encrypted message: {encrypted_message}")

            case 3:
                message = input("Type your encrypted message: ")
                decrypted_message = ""
                for letter in message:
                    if letter in key:
                        index = key.index(letter)
                        decrypted_message += chars[index]
                    else:
                        decrypted_message += letter
                print(f"Decrypted message: {decrypted_message}")

            case 4:
                print("Exiting the program...")
                break

            case _:
                print("Invalid option. Please select a number between 1 and 4.")

if __name__ == "__main__":
    menu(chars, key)

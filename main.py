import password_manager
from utils import generate_password,encrypt_message,decrypt_message

def menu():
    while True:
        print()
        print("=-"*20)
        print("MENU".center(40))
        print("=-"*20)
        print("[1] Generate a new password")
        print("[2] Encrypt a message")
        print("[3] Decrypt a message")
        print("[4] Password manager")
        print("[5] Exit")
        choice = input("Select an option\n>>> ")

        match choice:
            case "1":
                generate_password()
            case "2":
                encrypt_message()
            case "3":
                decrypt_message()
            case "4":
                password_manager.run()
            case "5":
                print("Exiting program...")
                break
            case _:
                print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    menu()
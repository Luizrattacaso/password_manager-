from utils import (generate_password,encrypt_message,decrypt_message,set_master_password,
    verify_master_password,add_account,delete_account,list_accounts,retrieve_password)

def main_menu():
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
        choice = input("Select an option:\n>>> ")

        match choice:
            case "1":
                generate_password()
            case "2":
                encrypt_message()
            case "3":
                decrypt_message()
            case "4":
                passwords_menu()
            case "5":
                print("Exiting program...")
                break
            case _:
                print("Invalid option. Please choose between 1 and 5.")
    
def passwords_menu():
    """Menu principal do gerenciador de senhas."""
    while True:
        print("\n[1] Enter")
        print("[2] Set master password")
        print("[3] Return to the main program")
        choice = input("Select an option:\n>>> ")

        match choice:
            case "1":
                if verify_master_password():
                    while True:
                        print("\n[1] Add account")
                        print("[2] Delete account")
                        print("[3] List accounts")
                        print("[4] Retrieve password")
                        print("[5] Back to menu")
                        option = input("Select an option:\n>>> ")

                        match option:
                            case "1":
                                add_account()
                            case "2":
                                delete_account()
                            case "3":
                                list_accounts()
                            case "4":
                                list_accounts()
                                try:
                                    idx = int(input("Account number: "))
                                    retrieve_password(idx)
                                except ValueError:
                                    print("Please enter a valid number.")
                            case "5":
                                break
                            case _:
                                print("Invalid option.")
            case "2":
                set_master_password()
            case "3":
                print("Exiting...")
                break
            case _:
                print("Invalid option.")

if __name__ == "__main__":
    main_menu()
from getpass import getpass #getpass hide the letters in user's input
import json
import os
from cryptography.fernet import Fernet
import bcrypt

def load_or_create_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
    else:
        with open("key.key", "rb") as f:
            key = f.read()
    return Fernet(key)

fernet = load_or_create_key()

DATA_FILE = "passwords.json"

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"master_password_hash": None, "accounts": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def set_master_password():
    password = getpass("Enter your new master password: ")
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    data = load_data()
    data["master_password_hash"] = hashed.decode()
    save_data(data)
    print("Master password set successfully!")

def verify_master_password():
    data = load_data()
    if data["master_password_hash"] is None:
        print("Master password not set yet.")
        return False
    password = getpass("Enter your master password: ")
    if bcrypt.checkpw(password.encode(), data["master_password_hash"].encode()):
        return True
    else:
        print("Incorrect password.")
        return False

def add_account():
    name = input("Account name: ")
    username = input("Username: ")
    password = getpass("Password: ")
    encrypted_password = fernet.encrypt(password.encode()).decode()

    data = load_data()
    data["accounts"].append({
        "name": name,
        "username": username,
        "password": encrypted_password
    })
    save_data(data)
    print("Account added successfully.")

def list_accounts():
    data = load_data()
    for i, account in enumerate(data["accounts"]):
        print(f"{i + 1}. {account['name']}")

def retrieve_password(index):
    data = load_data()
    account = data["accounts"][index - 1]
    decrypted_password = fernet.decrypt(account["password"].encode()).decode()
    print(f"Password: {decrypted_password}")

def main_menu():
    while True:
        print("\n[1] Enter")
        print("[2] Set master password")
        print("[3] Exit the program")
        choice = input(">>> ")

        if choice == "2":
            set_master_password()
        elif choice == "1":
            if verify_master_password():
                while True:
                    print("\n[1] Add account")
                    print("[2] List accounts")
                    print("[3] Retrieve password")
                    print("[4] Back to main menu")
                    option = input(">>> ")

                    match option:
                        case "1":
                            add_account()
                        case "2":
                            list_accounts()
                        case "3":
                            list_accounts()
                            try:
                                idx = int(input("Account number: "))
                                retrieve_password(idx)
                            except Exception:
                                print("Invalid option.")
                        case "4":
                            break
                        case _:
                            print("Invalid option.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
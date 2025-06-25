from getpass import getpass
import json
import os
from cryptography.fernet import Fernet
import bcrypt

def load_or_create_key():
    """Carrega ou cria uma nova chave Fernet para criptografia simétrica."""
    key_file = "key.key"
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    else:
        with open(key_file, "rb") as f:
            key = f.read()
    return Fernet(key)

fernet = load_or_create_key()

DATA_FILE = "passwords.json"

def save_data(data):
    """Salva os dados criptografados no arquivo JSON."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"master_password_hash": None, "accounts": []}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Data file corrupted. Resetting...")
        return {"master_password_hash": None, "accounts": []}


def set_master_password():
    """Define ou redefine a senha mestra protegida por hash bcrypt."""
    data = load_data()

    if data["master_password_hash"] is None:
        print("Setting the master password for the first time.")
        password = getpass("Enter your new master password: ")
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        data["master_password_hash"] = hashed.decode()
        save_data(data)
        print("Master password set successfully!")
    else:
        print("Changing the existing master password.")
        if verify_master_password():
            new_password = getpass("Enter your new master password: ")
            hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
            data["master_password_hash"] = hashed.decode()
            save_data(data)
            print("Master password changed successfully!")
        else:
            print("Password verification failed. Cannot change master password.")


def verify_master_password():
    """Verifica se a senha mestra informada está correta."""
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
    """Adiciona uma nova conta ao gerenciador com credenciais criptografadas."""
    name = input("Account name: ").strip()
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()

    if not name or not username or not password:
        print("All fields are required.")
        return

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
    """Lista todas as contas salvas."""
    data = load_data()
    if not data["accounts"]:
        print("No accounts found.")
        return
    for i, account in enumerate(data["accounts"], start=1):
        print(f"{i}. {account['name']}")


def retrieve_password(index):
    """Recupera e exibe a senha de uma conta específica."""
    data = load_data()
    try:
        account = data["accounts"][index - 1]
        decrypted_password = fernet.decrypt(account["password"].encode()).decode()
        print(f"Password: {decrypted_password}")
    except IndexError:
        print("Invalid account number.")
    except Exception as e:
        print(f"Error retrieving password: {e}")

def main_menu():
    """Menu principal do gerenciador de senhas."""
    while True:
        print("\n[1] Enter")
        print("[2] Set master password")
        print("[3] Return to the main program")
        choice = input(">>> ")

        match choice:
            case "1":
                if verify_master_password():
                    while True:
                        print("\n[1] Add account")
                        print("[2] List accounts")
                        print("[3] Retrieve password")
                        print("[4] Back to menu")
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
                                except ValueError:
                                    print("Please enter a valid number.")
                            case "4":
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

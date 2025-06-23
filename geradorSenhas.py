import random
import string

chars = list(string.punctuation + string.digits + string.ascii_letters)

n = 1
while n == 1:
    print()
    print("-="*30)
    print("MENU".center(60))
    print("-="*30)
    print("[1] Create a new password.")
    print("[2] Encrypt a message")
    print(f"[3] Exit\n")

    option = int(input("Select your option: "))

    if option == 1:
        chacters = int(input("How many charcters do you want in your new password? "))
        newPassword = ""
        for char in range(chacters):
            newPassword += random.choice(chars)
        
        print(f"Here is your new password: {newPassword}")

    if option == 2:
        chars = list(" " + string.punctuation + string.digits + string.ascii_letters)
        message = input("Text your message: ")
        Encrypted = []
        newMessage = ""
        for i in range(len(chars)):
            aux = random.choice(chars)
            Encrypted.append(aux)
        for letter in message:
            newMessage += random.choice(Encrypted)
        print(f"Encrypted message: {newMessage}")
    n = 2


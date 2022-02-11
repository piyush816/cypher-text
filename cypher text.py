
def encrypt(key, message):
    encrypted_message = ""
    for char in message:
        try:
            encrypted_message += chr(ord(char) + key)
        except Exception as e:
            print(f"Error {e}")
            break

    return encrypted_message


def decrypt(key, message):
    decrypted_message = ""
    for char in message:
        try:
            decrypted_message += chr(ord(char) - key)
        except Exception as e:
            print(f"Error {e}")
            break
    return decrypted_message


if __name__ == '__main__':

    run = True

    while run:
        choice = input("(e) for encrypt and (d) for decrypt and (q) to quit: ").lower()
        if choice == "q":
            break

        elif choice == "e":
            key = int(input("Enter key: "))
            message = input("Enter Message: ")
            print(encrypt(key, message))

        elif choice == "d":
            key = int(input("Enter Encryption key: "))
            message = input("Enter Encrypted Message: ")
            print(decrypt(key, message))

        else:
            print("Invalid choice")

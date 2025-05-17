def caesar_cipher(text, key, mode):
    result = ""

    for char in text:
        if char.isalpha():
           
            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                shifted = chr((ord(char) - base + key) % 26 + base)
            elif mode == "decrypt":
                shifted = chr((ord(char) - base - key) % 26 + base)

            result += shifted
        else:
            
            result += char

    return result

print("Caesar Cipher")
print("Choose an option:")
print("A Encrypt a message")
print("B Decrypt a message")

choice = input("Enter A or B: ")

if choice == "A":
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the key (number to shift): "))
    encrypted = caesar_cipher(message, key, "encrypt")
    print("Encrypted message:", encrypted)

elif choice == "B":
    message = input("Enter the message to decrypt: ")
    key = int(input("Enter the key (number used during encryption): "))
    decrypted = caesar_cipher(message, key, "decrypt")
    print("Decrypted message:", decrypted)

else:
    print("Invalid choice.")

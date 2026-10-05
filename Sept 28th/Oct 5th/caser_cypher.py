


def encrypt(char, shift):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        index = alphabets.index(char.lower())
        new_index = (index + shift) % len(alphabets)

        if char.islower():
            return alphabets[new_index]
        else:
            return alphabets[new_index].upper()
    else:
        return char

    


def decrypt(text, shift):
    return encrypt(text, -shift)


message = list(input("Enter the word you want to cipher: "))
while True:
    cipher = input("encrypt or decrypt: ").lower()
    if cipher in ("encrypt","decrypt"):
        break
while True:
    try:
        shift = int(input("Enter your shift (integer): "))
        break
    except:
        print("Must be a whole number")


print(f"Original: {"".join(message)}")
if cipher == "encrypt":
    encrypted = "".join(list(map(lambda char: encrypt(char, shift), message)))
    print(f"Encrypted: {encrypted}")
else:
    decrypted = "".join(list(map(lambda char: decrypt(char, shift), message)))
    print(f"Decrypted: {decrypted}")

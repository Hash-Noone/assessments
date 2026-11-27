# Caesar cipher using manual alphabet indexes and modulo overflow

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(text, shift):
    result = []

    for char in text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            new_index = (index + shift) % len(alphabet)

            if char.islower():
                result.append(alphabet[new_index])
            else:
                result.append(alphabet[new_index].upper())
        else:
            result.append(char)

    return "".join(result)


def decrypt(text, shift):
    return encrypt(text, -shift)


message = "Hello, World!"
s = 3
encrypted = encrypt(message, s)
decrypted = decrypt(encrypted, s)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

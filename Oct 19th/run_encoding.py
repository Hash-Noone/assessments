def encoding(string):
    right = 0
    left = 0
    new = []
    while right < len(string):
        while right < len(string) and string[left] == string[right]:
            right += 1
        new.append(string[left])
        new.append(str(right - left))
        left = right
    return "".join(new)

def decoding(string):
    right = 1
    left = 0
    new = []
    while right < len(string):
        while right < len(string) and "0" <= string[right] <= "9":
            right += 1
        new.append(string[left] * int(string[left + 1: right]))
        left = right
        right = left + 1
    return "".join(new)

text = input("Enter the characters you want to decode or encode: ")
choice = input("Enter 1 for encode or 2 for decode")
if choice == "1":
    print(encoding(text))
elif choice == "2":
    print(decoding(text))
else:
    print("Wrong choice")
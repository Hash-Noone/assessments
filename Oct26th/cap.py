sentence = input("Enter your sentence here: ").split()
cap = []
for word in sentence:
    if 'a' <= word[0] <= 'z':
        cap.append(chr(ord(word[0]) - 32) + word[1:])
print(f"""Capitalized: {" ".join(cap)}
No Spaces: {"".join(cap)}""")
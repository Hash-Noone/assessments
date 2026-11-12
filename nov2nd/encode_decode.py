def encode(string):
    if not string:
        return ""
    prev = string[0]
    count = 1
    result = []
    for char in string[1:]:
        if char != prev:
            result.append(prev + str(count))
            prev, count = char, 1
        else:
            count += 1
    result.append(prev + str(count))
    return "".join(result)

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

tests = [
    "AAAAABBBCC",
    "A",
    "AAAAAAAAAA",
    "AAABBBBBCCCC",
    ""
]

for original in tests:
    encoded = encode(original)
    decoded = decoding(encoded)

    print(original, encoded, decoded)
    assert original == decoded
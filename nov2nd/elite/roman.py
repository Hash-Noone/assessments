roman_dict = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
    "V̄" : 5000,
}

roman = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

def number_to_roman(num):
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("Only integers are allowed")
    if not (1 <= num <= 3999):
        raise ValueError("Numbers between one and 3999 are allowed inclusive")
    result = []
    for value, symbol in roman:
        count, num = divmod(num, value)
        result.append(symbol * count)
    return "".join(result)

def roman_to_number(s):
    if not isinstance(s, str):
        raise TypeError("Only strings are allowed")
    if not s:
        raise ValueError("Must contains at least a character")
    total = prev = 0

    for char in reversed(s):
        value = roman_dict.get(char, 0)

        if not value:
            return "Invalid Input"

        total += -value if value < prev else value
        prev = max(prev, value)

    return total
    
print(number_to_roman(3999))
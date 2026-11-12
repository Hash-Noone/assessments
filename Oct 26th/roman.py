roman = {
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
}

def roman_to_number(s):
    total = prev = 0

    for char in reversed(s):
        value = roman.get(char, 0)

        if not value:
            return "Invalid Input"

        total += -value if value < prev else value
        prev = max(prev, value)

    return total

num = 0
sentence = input("Enter your roman numeral here: ").upper()
print(roman_to_number(sentence))

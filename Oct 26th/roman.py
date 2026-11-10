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

def roman_to_number(char):
    prev = 0
    res = 0
    for index in range(len(char)-1,-1,-1):
        if char[index] in roman:
            if prev > roman[char[index]]:
                res -= roman[char[index]]
            else:
                res += roman[char[index]]
                prev = roman[char[index]]
        else:
            return "Invalid Input"
    return res

num = 0
sentence = input("Enter your roman numeral here: ").upper()
print(roman_to_number(sentence))

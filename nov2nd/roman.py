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
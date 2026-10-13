def compose(*functions):
    def apply(value):
        result = value
        for index in range(len(functions)-1,-1,-1):
            result = functions[index](result)
        return result
    return apply


def pipe(*functions):
    def apply(value):
        result = value
        for func in functions:
            result = func(result)
        return result
    return apply


def strip(value):
    return value.strip()


def lower(value):
    return value.lower()


def remove_vowels(value):
    vowels = "aeiou"
    return "".join(char for char in value if char.lower() not in vowels)


def reverse(value):
    if len(value) == 1:
        return value
    return value[-1] + reverse(value[:-1])

add_one = lambda x: x + 1
double = lambda x: x * 2
print(compose(add_one, double)(5))
print(pipe(add_one, double)(5))

pipeline = pipe(strip, lower, remove_vowels, reverse)
print(pipeline("  Hello World  "))

def encode(string):
    if not string:
        return ""
    prev = string[0]
    count = 0
    result = ""
    for char in string:
        if char != prev:
            result += prev + str(count)
            prev, count = char, 1
        else:
            count += 1
    result += prev + str(count)
    return result

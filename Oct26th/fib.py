while True:
    try:
        number = int(input("Enter your valid number: "))
        break
    except ValueError:
        print("Enter a valid integer")
num = 2
pre = 0
prev = 1
result = "0,1"
eve_sum = 0
while num < number:
    temp, prev = prev, prev + pre
    pre, result = temp, result + "," + str(prev)
    if prev % 2 == 0:
        eve_sum += prev
    num += 1
rev = ""
index = 0
while index < len(result):
    start = index
    while index  < len(result) and result[index] != ",":
        index += 1
    rev = result[start:index] + "," + rev
    index += 1
rev = rev[:-1]
if number > 1:
    print(f"""Sequence: {result}
Even Sum: {eve_sum}
Reversed: {rev}""")
else:
    print(f"""Sequence: 0
    Even Sum: {eve_sum}
    Reversed: 0""")

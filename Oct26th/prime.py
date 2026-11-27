def prime(num:int):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0 :
        return False
    n = 3
    while n <= int(num ** 0.5):
        if num % n == 0:
            return False
        n += 2
    return True 

def prime_printer(num:int):
    if prime(num):
        return f"{num} is prime."
    return f"{num} is not prime."
    

while True:
    try:
        number = int(input("Enter your valid number: "))
        break
    except ValueError:
        print("Enter a valid integer")
print(prime_printer(number))
num = 3
arr = [2]
total = 2
while num <= number:
    if prime(num):
        arr.append(num)
        total += num
    num += 2
if num >= 2:
    print(f"Primes up to {number}: {arr}")
    print(f"Sum of primes: {total}")
else:
    print("No prime number before this number")

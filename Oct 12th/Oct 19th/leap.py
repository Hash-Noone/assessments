def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

while True:    
    try:
        year = int(input("Enter the year you want to check: "))
        if year < 1:
            print("Cannot have negative or zero years")
            continue
        break
    except ValueError:
        print("Enter a number")
years = []
if leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

while len(years) < 3:
    year += 1
    if leap_year(year):
        print(f"{year} is a leap year")
        years.append(year)

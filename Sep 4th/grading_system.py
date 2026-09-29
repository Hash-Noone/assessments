def calculate_average(grades):
    count = 0
    total = 0
    for grade in grades:
        total += grade
        count += 1
    return total / count

students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68],
    ["Mary", 45, 50, 45],
]

grade_results = {70: "A", 60: "B", 50: "C", 45: "D", 40: "E", 0: "F"}

for student in students:
    name = student[0]
    grades = student[1:]
    average = round(calculate_average(grades), 2)
    print(f"{name}- Average: {average: .2f}- Grade: {grade_results[next(key for key in sorted(grade_results.keys(), reverse=True) if average >= key)]}")


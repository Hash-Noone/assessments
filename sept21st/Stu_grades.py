def calculate_grade(average):
    if average >= 70:
        return "A"
    if average >= 60:
        return "B"
    if average >= 50:
        return "C"
    if average >= 45:
        return "D"
    if average >= 40:
        return "E"
    return "F"

students = [["Samuel", 80, 75, 90], 
            ["David", 55, 60, 50], 
            ["Mary", 35, 40, 30], 
            ["John", 65, 70, 68], 
            ["Moses",90,80,70,60]]

for student in students:
    total = 0
    name = student[0]
    for score in student[1:]:
        total += score
    average = round((total)/len(student[1:]),2)
    grade = calculate_grade(average)
    print(f"{name} → Average: {average:.2f} → Grade: {grade} \n")
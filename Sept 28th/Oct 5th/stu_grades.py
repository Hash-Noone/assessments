def grade_for(average):
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

students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]},
    {"name": "Davies", "scores": [55, 60, 50]}, 
    {"name": "Mary", "scores": [35, 40, 30]}, 
    {"name": "John", "scores": [65, 70, 68]}, 
    {"name": "Moses", "scores": [90,80,70,60]}
]
result = []
for student in students:
    total = 0
    for score in student["scores"]:
        total += score
    average = round(total/len(student["scores"]),2)
    result. append([student["name"],average])
result_with_grade = list(map(lambda student: (student[0], student[1], grade_for(student[1])), result))
print(result_with_grade)
result_above_D = list(filter(lambda student: student[2] in "ABC" , result_with_grade))
print(result_above_D)
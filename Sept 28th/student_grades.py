students = [{"name": "Sam", "scores": [80, 90]}, 
            {"name": "Sam", "scores": [80, 90]}, 
            {"name": "Sam", "scores": [80, 90]}, 
            {"name": "Sam", "scores": [80, 90]}, 
            {"name": "David", "scores": [55, 60]}]

top_student = ["", 0 , ""]
worse_student = ["", 100, ""]
for student in students:
    total_score = 0
    count = 0
    for score in student["scores"]:
        total_score += score
        count += 1
    average_score = total_score / count
    if average_score > 70:
        grade = "A"
    elif average_score > 60:
        grade = "B"
    elif average_score > 50:
        grade = "C"
    elif average_score > 45:
        grade = "D"
    elif average_score > 40:
        grade = "E"
    else:
        grade = "F" 
    print(f"{student["name"]} - Average: {average_score: .2f} - Grade:{grade}")
    if average_score > top_student[1]:
        top_student[1] = average_score
        top_student[0] = student["name"]
        top_student[2] = grade
    if average_score < worse_student[1]:
        worse_student[1] = average_score
        worse_student[0] = student["name"]
        worse_student[2] = grade

print(f"The best student is {top_student[0]} with the average score {top_student[1]} and grade {top_student[2]}")

print(f"The worse student is {worse_student[0]} with the average score {worse_student[1]} and grade {worse_student[2]}")

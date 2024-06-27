student_scores = {
    "john": 93,
    "carry": 34,
    "alex": 78,
    "smith": 90,
    "roy": 67,
    "kumar": 56
}
student_grade = {}
for student in student_scores:
    score=student_scores[student]
    if score > 89:
        student_grade[student] = "outsatanding"
    elif score > 75:
        student_grade[student] = "Excellent"
    elif score > 65:
        student_grade[student] = "very good"
    elif score > 50:
        student_grade[student] = "Pass"
    else:
        student_grade[student] = "Fail"

print(student_grade)
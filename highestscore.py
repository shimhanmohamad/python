student_scores = input("Input a list of student marks : ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max_marks = 0
for score in student_scores:
    if score > max_marks:
        max_marks = score
print(f"The highest marks in the class : {max_marks}")


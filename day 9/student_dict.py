student_scores={
    "michelle":70,
    "jpeace":75,
    "wilson":74,
    "victor":79,
    "hope":89,
    "kayode":20
}

student_grades={}

for student in student_scores:
    scores=student_scores[student]
    if scores > 90:
        student_grades[student] = "Outstanding"
    elif scores > 80:
        student_grades[student] = "Exceeds Expectations"
    elif scores >= 70:
        student_grades[student] = "Acceptable"
    else:
     student_grades[student]="Fail"

print(student_grades)
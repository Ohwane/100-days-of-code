student_heights=input("input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n]=int(student_heights[n])
print(student_heights)
total_height=0
for height in student_heights:
    total_height+=int(height)
print(total_height)

number_students=0
for number in student_heights:
    number_students+=1
print(number_students)

tallest_student=0
for t in student_heights:
    t=int(t)
    if t > tallest_student:
        tallest_student=t
print(tallest_student)
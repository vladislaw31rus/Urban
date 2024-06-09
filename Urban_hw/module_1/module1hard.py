# Задание "Средний балл"
n = int(input("Enter the numder of students :"))
students = []
grades = []
avg_grade = []
for _ in range(n):
    students.append(input("Enter student name :"))
    marks = input("Enter grades separated by spaces :").split()
    marks = [int(item) for item in marks]
    grades.append(marks)
    avg_grade.append(sum(marks) / len(marks))
zipped = zip(students, avg_grade)
students_and_avg_grades = dict(zipped)
sort_students_and_avg_grades = sorted(students_and_avg_grades.items())
sort_students_and_avg_grades = dict(sort_students_and_avg_grades)
print("Students and average grade :",sort_students_and_avg_grades)
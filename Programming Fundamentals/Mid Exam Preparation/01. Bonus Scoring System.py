students = int(input())
lectures = int(input())
bonus = int(input())
total_bonus = 0
max_bonus = 0
attendance_current_student = 0

for current_student in range(students):
    attendance = int(input())
    total_bonus = attendance / lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attendance_current_student = attendance

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {attendance_current_student} lectures.")

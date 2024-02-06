def softuni_students(*students, **course) -> str:
    invalid_students = []
    result = []

    for student_id, username in sorted(students, key=lambda x: x[1]):
        if student_id in course.keys():
            result.append(f"*** A student with the username {username} has successfully finished the course {course[student_id]}!")
        else:
            invalid_students.append(username)

    formatted_result = "\n".join(result)

    if invalid_students:
        formatted_result += f"\n!!! Invalid course students: {', '.join(invalid_students)}"

    return formatted_result
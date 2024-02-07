def gather_credits(credits, *course_info):
    courses = []
    credits_shortage = 0

    for course_name, course_credits in course_info:
        if credits_shortage >= credits:
            break

        if course_name not in courses:
            courses.append(course_name)
            credits_shortage += course_credits

    if credits_shortage >= credits:
        return f"Enrollment finished! Maximum credits: {credits_shortage}.\nCourses: {', '.join(sorted(courses))}"
    return f"You need to enroll in more courses! You have to gather {credits - credits_shortage} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

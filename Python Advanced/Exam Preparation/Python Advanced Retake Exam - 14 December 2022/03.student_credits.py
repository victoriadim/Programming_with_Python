def students_credits(*info):
    total_credits_count = 0
    output = {}
    for _ in info:

        course_name, max_credits_course, max_points, diyans_points = [int(x) if x.isdigit() else x for x in input().split("-")]
        percentage = diyans_points / max_points
        curr_credits = max_credits_course * percentage
        total_credits_count += curr_credits
        output[course_name] = curr_credits

    sorted_courses = dict(sorted(output.items(), key=lambda x: (x[1], x[0]), reverse=True))
    result = ''
    if total_credits_count >= 240:
        result += f"Diyan gets a diploma with {total_credits_count:.1f} credits."'\n'
    else:
        result += f"Diyan needs {(240 - total_credits_count):.1f} credits more for a diploma."'\n'

    for course, course_credits in sorted_courses.items():
        result += f"{course} - {course_credits:.1f}\n"

    return result

# def students_credits(*args):
#     total_credits = 0
#     result = {}
#     for data in args:
#
#         course, max_credits, max_points, d_points = [int(x) if x.isdigit() else x for x in data.split('-')]
#         percentage = d_points / max_points
#         current_credits = percentage * max_credits
#         total_credits += current_credits
#         result[course] = current_credits
#
#     sorted_courses = dict(sorted(result.items(), key=lambda x: (x[1], x[0]), reverse=True))
#     output = ''
#     if total_credits >= 240:
#         output += f"Diyan gets a diploma with {total_credits:.1f} credits."'\n'
#     else:
#         output += f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma."'\n'
#
#     for course, course_credits in sorted_courses.items():
#         output += f"{course} - {course_credits:.1f}\n"
#
#     return output


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

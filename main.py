from canvasapi import Canvas
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv('API_URL')

canvas = Canvas(API_URL,API_KEY)

course = canvas.get_course(144)

enrollments = course.get_enrollments(user_id=216, type=["StudentEnrollment"])
my_enrollment = enrollments[0]

print(my_enrollment.grades['current_score'])
print(my_enrollment.grades['current_grade'])

courses = canvas.get_courses()

listofusers = []

for course in courses:
    print(f"{course.name}: {course.id}")
    for user in course.get_users(enrollment_type=['student']):
        print(f"{user.name}: {user.id}")
        listofusers.append(user.id)
    enrollments = course.get_enrollments(user_id=216, type=["StudentEnrollment"])
    my_enrollment = enrollments[0]

    print(f"Grade: {my_enrollment.grades['current_score']}%")
    print(my_enrollment.grades['current_grade'])


newlist = list(set(listofusers))

newlist.sort()

print(newlist)



# course = canvas.get_course(354)

# for user in course.get_users(enrollment_type=['student']):
#     print(f"{user.name}: {user.id}")

# tester = canvas.get_user(1)

# print(user.name)
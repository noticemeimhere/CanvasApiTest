from canvasapi import Canvas
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv('API_URL')

canvas = Canvas(API_URL,API_KEY)

courses = canvas.get_courses()

listofusers = []

for course in courses:
    print(f"{course.name}: {course.id}")
    for user in course.get_users(enrollment_type=['student']):
        listofusers.append(user.id)
        # print(f"{user.name}: {user.id}")


newlist = list(set(listofusers))

newlist.sort()

print(newlist)



# course = canvas.get_course(354)

# for user in course.get_users(enrollment_type=['student']):
#     print(f"{user.name}: {user.id}")

# tester = canvas.get_user(1)

# print(user.name)
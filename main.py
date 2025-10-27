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

courses = canvas.get_courses()
user = course.get_users

for course in courses:
    users = course.get_users()
    for user in users:
        print(user)


#returns a gpa score from a grade
def get_gpa_from_grade(grade):
    if grade >= 93:
        gpa = 4.0
    elif grade >= 90:
        gpa = 3.7
    return gpa

for course in courses:
    
    enrollments = course.get_enrollments(user_id=216, type=["StudentEnrollment"])
    my_enrollment = enrollments[0]
    grade = my_enrollment.grades['current_score']

    if grade == None:
        pass
    else:
        print(f"\n{course.name}: {course.id}")
        print(f"Grade: {my_enrollment.grades['current_score']}%")
        print(get_gpa_from_grade(grade))
        

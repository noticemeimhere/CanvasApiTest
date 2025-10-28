from canvasapi import Canvas
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv('API_URL')

canvas = Canvas(API_URL,API_KEY)

course = canvas.get_course(144)

courses = canvas.get_courses()
print(courses)

gpalist = []

print(canvas.get_user(216))

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
    elif grade >= 87:
        gpa = 3.3
    elif grade >= 83:
        gpa = 3
    elif grade >= 80:
        gpa = 2.7
    elif grade >= 77:
        gpa = 2.3
    elif grade >= 73:
        gpa = 2
    elif grade >= 70:
        gpa = 1.7
    elif grade >= 67:
        gpa = 1.3
    elif grade >= 60:
        gpa = 1
    else:
        gpa = 0
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
        gpalist.append(get_gpa_from_grade(grade))
        
print(round(sum(gpalist)/7,2))
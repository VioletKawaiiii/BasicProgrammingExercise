# Program created by Muhammad Fikry Haikal
# Class TI22I

from time import sleep
import os


def display(grades):
    s_len = 70
    pattern = " {:<3} {:<20} {:<8} {:<15} {:<0}"

    print("-" * s_len)
    print(pattern.format("NO", "COURSE", "GRADE" , "LETTER VALUE", "PREDICATE"))

    for idx, grade in enumerate(grades):
        result = check_grade(grade=grade["grade"])
        course = grade["course"]
        letter_value = result[0]
        predicate = result[1]

        print("-" * s_len)
        print(pattern.format(idx + 1, course, grade["grade"], letter_value, predicate))
        print("-" * s_len)



def check_grade(grade):

    if grade >= 90 and grade <= 100:
        return ("A", "With compliment")
    elif grade >= 80 and grade <= 89:
        return ("B", "Very satisfy")
    elif grade >= 70 and grade <= 79:
        return ("C", "Satisfying")
    elif grade >= 60 and grade <= 69:
        return ("D", "Not satisfactory")
    elif grade >= 0 and grade <= 59:
        return ("E", "Not pass")
    else:
        return ("Error", "Invalid grade value")


def get_grade():
    grades = []

    print("Enter 'e' or 'E' to exit the form")

    while True:
        grade_object = {}

        course = input("Enter course name: ")

        if course == 'e' or course == "E":
            break

        grade = input('Enter your grade: ')

        if grade.isnumeric() and not course.isnumeric():
            grade_object["course"] = course
            grade_object["grade"] = float(grade)
            grades.append(grade_object)
        else:
            print("ERROR")
            
    os.system('cls')
    return grades
    
    
def main():
    grades = get_grade()

    if len(grades):
        display(grades=grades)
    else:
        print("Not have data")
        sleep(1)

main()

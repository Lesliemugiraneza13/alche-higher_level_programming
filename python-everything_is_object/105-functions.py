#!/usr/bin/python3
def add_subject(student_list):
    student_list.append("Math")

def change_name(name):
    name = "Someone Else"

subjects = ["English", "Science"]
add_subject(subjects)
print(subjects)

student_name = "Marlene"
change_name(student_name)
print(student_name)

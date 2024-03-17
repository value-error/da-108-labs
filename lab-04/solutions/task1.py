def get_non_zero_string(prompt):
    while True:
        s = input(prompt)
        s = s.strip()
        if s: return s

def get_positive_integer(prompt, error_message):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                raise ValueError("number must be positive")
            return n
        except ValueError as e:
            print("error: %s" % error_message)

def get_grade(marks):
    if marks >= 90: return "A"
    elif marks >= 80: return "B"
    elif marks >= 70: return "C"
    elif marks >= 60: return "D"
    else: return "F"

student_name = get_non_zero_string("Enter Student Name: ")
roll_no = get_positive_integer("Enter Roll No: ", "invalid roll number")
marks_maths = get_positive_integer("Enter marks in Maths: ", "invalid marks")
marks_physics = get_positive_integer("Enter marks in Physics: ", "invalid marks")
marks_chemistry = get_positive_integer("Enter marks in Chemistry: ", "invalid marks")

marks_avg = (marks_maths + marks_physics + marks_chemistry) / 3

print("")
print("-" * 20)
print("")

print("Student Name:", student_name)
print("Student Roll:", roll_no)
print("Grade in Maths:", get_grade(marks_maths))
print("Grade in Physics:", get_grade(marks_physics))
print("Grade in Chemistry:", get_grade(marks_chemistry))
print("Overall Grade:", get_grade(marks_avg))


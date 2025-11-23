import pandas as pd

grade_number = {
    "A": 4.0,
    "A-": 3.667,
    "B+": 3.333,
}

courses = pd.read_csv("calculate_gpa/courses.csv")
courses['num_grade'] = courses['Grade'].apply(lambda a: grade_number[a])


courses['major'] = courses['Course Name'].apply(lambda x: True if (
    x[:2] == "CS" or x[:4] == "MATH" or x[:2] == "IS" or x[:2] == "DS") else False)

major_courses = courses[courses['major'] == True]
total_credits = major_courses['Credits'].sum()
major_courses['rel_weight'] = major_courses['Credits'] / total_credits

major_courses['total'] = major_courses['rel_weight'] * \
    major_courses['num_grade']

print(f"Major GPA: {major_courses['total'].sum()}")
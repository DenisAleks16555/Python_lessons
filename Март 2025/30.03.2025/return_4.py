def convert_to_5grade(grade):
    new_grade = None
    if grade >= 10:
        new_grade = 5
    elif grade >= 7:
        new_grade = 4
    elif grade >= 4:
        new_grade = 3
    else:
        new_grade = 2
    return new_grade
 
print(convert_to_5grade(12))
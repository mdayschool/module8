
def switch_average(grade):
    grades = {'A':90, 'B':80, 'C':70, 'D':60, 'F':50}
    if grade in grades:
        return grades[grade]
    else:
        raise ValueError(grade + " is not a recognized grade.")

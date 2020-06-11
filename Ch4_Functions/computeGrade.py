"""
every function has a declaration, can/cannot have arguments, can/cannot have return value and needs to be called.

"""

def computeGrade(score):
    try:
        if float(score) > 1.0:
            grade = 'Bad score'
        elif float(score) >= 0.9:
            grade = 'A'
        elif float(score) >= 0.8:
            grade = 'B'
        elif float(score) >= 0.7:
            grade = 'C'
        elif float(score) >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
    except:
        grade = 'Bad score'
    return grade

print(computeGrade(0.4))
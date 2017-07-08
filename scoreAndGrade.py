'''
    scoreAndGrade.py
    Leif Anderson 7/8/17
'''
import random

def convertGradeValToLetter(grade):
    letterGrade = ''
    if grade < 70:
        letterGrade = 'D'
    elif grade < 80:
        letterGrade = 'C'
    elif grade < 90:
        letterGrade = 'B'
    else:
        letterGrade = 'A'
    return letterGrade

def scoresAndGrades():
    print 'Scores and Grades'
    grade = 0.0
    for i in range(0, 10):
        grade = random.randint(60, 100)
        print "Score: " + str(grade) + "; Your grade is " + convertGradeValToLetter(grade)
    print 'End of the program. Bye!'

scoresAndGrades()

# Dora Jambor, dorajambor@gmail.com
# gpa.py
# 5.12.2014

'''
Calculates GPA
'''

# get name and grades list
def GetInfo():
    name = raw_input("Student's name: ")
    gr1 = raw_input("Enter a grade:  ")
    gr2 = raw_input("Enter a grade:  ")
    gr3 = raw_input("Enter a grade:  ")
    gr4 = raw_input("Enter a grade:  ")
    return name, gr1, gr2, gr3, gr4

# map grades to values
grademap = { 'A': 4, 'B': 3, 'C': 2, 'D': 1 }

# convert grades list to integers
def grade_to_int(x):
    try:
        return grademap[x.upper()]
    except KeyError:
        raise Exception('invalid grade: ' + x)

def GetGrades(grades):
    return map(grade_to_int, grades)

def CalcGPA(grades):
    return sum(grades)/len(grades)

def main(name, GPA):
    print "The GPA of", name, "is", GPA

def play():
    name, gr1, gr2, gr3, gr4 = GetInfo()
    grades = GetGrades([gr1, gr2, gr3, gr4])
    GPA = CalcGPA(grades)
    main(name, GPA)

play()

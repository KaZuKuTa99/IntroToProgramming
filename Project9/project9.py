#--------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #9
# Due---------December 5,2018
#
# This program computes semester averages and letter
# grades for this course. The program will input grade
# data from a file. The file will contain data for an 
# entire class of students.
#--------------------------------------------------------

#--------------------------------------------------------
# gradeletter(numgrade); Takes a numerical value as an 
# argument, numgrade, and assigns a letter grade for the
# value dependent on where it lies on the spectrum of
# values.
#--------------------------------------------------------
def gradeletter(numgrade):
    if numgrade >= 90:
        letter = 'A'
    elif numgrade >= 80:
        letter = 'B'
    elif numgrade >= 70:
        letter = 'C'
    elif numgrade >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter

#--------------------------------------------------------
# Bool(quiz_line); Takes a line from the lines in the
# text document and returns either Boolean value of true
# or false based on how many objects are in the list.
#--------------------------------------------------------
def bool(quiz_line):
    if len(quiz_line) >= 2:
        return True
    else:
        return False

#--------------------------------------------------------
# quiz_avg(quiz_line); Computes the average for the
# quiz lines in the text document
#--------------------------------------------------------
def quiz_avg(quiz_line):
    total = 0
    grades = quiz_line.split()
    length = len(grades)
    drop = 100
    for q in grades:
        partial = int(q.replace('.',''))
        total += partial
        if partial < drop:
            drop = partial
    if bool(grades):
        total = total - drop
        length -= 1
    return (total/length)

#--------------------------------------------------------
# project_avg(project_line); Computes the average for
# the project lines in the text document.
#--------------------------------------------------------
def project_avg(project_line):
    total = 0
    grades = project_line.split()
    length = len(grades)
    for q in grades:
        total += float(q)
    return (total/length)*10    

#--------------------------------------------------------
# test_avg(test_line); Computes the average for the test
# line using the weights of each item to be used in
# semester_avg function.
#--------------------------------------------------------
def test_avg(test_line):
    grades = test_line.split()
    first = float(grades[0])
    second = float(grades[1])
    final = float(grades[2])
    length = len(grades)
    total = (first*0.2)+(second*0.2)+(final*0.25)
    return total

#--------------------------------------------------------
# semester_avg(quizes,projects,tests); Computes the
# semester average given the averages for the quizzes,
# projects, and tests. Uses the weights of the items in
# the calculations.
#--------------------------------------------------------
def semester_avg(quizes,projects,tests):
    quizweight = quizes * 0.15
    projectweight = projects * 0.2
    testweight = tests
    return quizweight + projectweight + testweight

#--------------------------------------------------------
# main(); opens two seperate files(one for reading and
# one for writing) and computes and prints the semester
# average and letter grade for students in a class onto
# the second file.
#--------------------------------------------------------
def main():
    filename = input('Enter input file name:')
    outfile = input('Enter output file name:')
    inputFile = open(filename,'r')
    outputFile = open(outfile,'w')
    lines = inputFile.readlines()

    index = 0
    while index <= len(lines)-1:
        names = lines[index]
        quiz_scores = lines[index+1]
        project_scores = lines[index+2]
        test_scores = lines[index+3]
        
        quiz = quiz_avg(quiz_scores)
        project = project_avg(project_scores)
        test = test_avg(test_scores)
        total_avg = semester_avg(quiz,project,test)
        alphagrade = gradeletter(total_avg)
        
        outputFile.write('%-20s %6.1f %s \n'%(names.strip('\n'),total_avg,alphagrade),)
        index += 4
    inputFile.close()
    outputFile.close()
    return

#--------------------------------------------------------
# ______________________MAIN PROGRAM_____________________
#--------------------------------------------------------
main()

#--------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #6
# Due---------October 31,2018
#
# This program reads the file and computes/prints the semester 
# average and letter grade for each student.
#--------------------------------------------------------
file = input('Enter file name: ')

inputFile = open(file,'r')
total = 0
count = 0
index = 3

for line in inputFile:
    outlist = line.split(',')
    while index < 7:
        total += float(outlist[index])
        count += 1
        index += 1
    average = total/count
    if average < 60.0:
        grade = 'F'
    elif average >= 60.0 and average < 70.0:
        grade = 'D'
    elif average >= 70.0 and average < 80.0:
        grade = 'C'
    elif average >= 80.0 and average < 90.0:
        grade = 'B'
    else:
        grade = 'A'
    name = outlist[1] + ', ' + outlist[2]
    print(outlist[0],' %-20s'%name, ' %5.1f '%average, '%2s'%grade,sep='')
    total = 0
    count = 0
    index = 3

inputFile.close()

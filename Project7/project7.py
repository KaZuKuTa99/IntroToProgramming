#--------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #7
# Due---------November 14,2018
#
# This program uses a user created function to compute 
# an approximation of sin(x). It prompts the user to 
# enter the name of an input file and an output file. 
# The input file will contain a list of floating-point 
# numbers, one number per line. The program should input
# each number, compute its sine, and write the sine 
# (rounded to five decimal places)approximated to 20
# terms to the output file.
#--------------------------------------------------------

# ----------------------------------------------------
# Factorial using while-loop (WORKS)
# ----------------------------------------------------
def fact(n):
    factorial = 1
    count = 2
    while count <= n:
        factorial *= count
        count += 1
    return factorial

# ----------------------------------------------------
# Taylor series using for-loop;must use fact function
# (WORKS)
# ----------------------------------------------------
def sin(x,n):
    sine = 0
    for count in range(n+1):
        sign = (-1)**count
        pi = 22/7
        sine += sign*((x**((2*count)+1))/(fact((2*count)+1)))
    return sine

# ----------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------

filename = input("Enter source file name: ")
outname = input("Enter output file name: ")
infile = open(filename,"r")
outfile= open(outname,"w")

for line in infile:
    x = float(line)
    n = 20
    app = sin(x,n)
    outfile.write('%8.5f \n'%app)

infile.close()
outfile.close()

# I added this part to signal that the program finished.
print("Computation is complete.Please check your file directory.")

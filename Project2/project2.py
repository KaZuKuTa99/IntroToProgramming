#--------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #2
# Due---------September 19,2018
#
# This program computes and prints values for an annual
# account given input by the user for an initial
# investment, growth rate, and amount of years.
#--------------------------------------------------------

# Input amounts for the calculation
initial_investment=float(input("Initial investment -- "))
growth_rate=float(input("Annual growth rate -- "))
years=int(input("Number of years ----- "))

print()

for year in range(1,years+1):
    balance=initial_investment*(1+(growth_rate/100))**year
    print("Year ",year,": $%0.2f"%balance,sep="")
# I couldn't remember the formula for compound interest so I found
# this one online on an accounting website.

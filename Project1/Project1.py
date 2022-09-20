#--------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #1
# Due---------September 12,2018
#
# This program computes an itemized estimate for lawn
# mowing services.
#--------------------------------------------------------

length=int(input("Length of lot -- "))
width=int(input("Width of lot --- "))
size=int(input("Size of house -- "))

area=length*width
# 1 hr=3600s
# 3 sq ft./s
# (3600s/1 hr)*(3 sq ft./1s)=10800 sq ft./hr
grass_hour=10800

# $25/hr
cost_1=((area-size)/grass_hour)*25

# cost for one day for 26 weeks with a 5
# percent discount
cost_season=(cost_1*26)*0.95

print()
print("Size of lot -------------",area,"square feet")
# I had to reduce the amount of space between the $
# and the number to try to match it to the examples.
print("Cost for one mowing ----- $%5.2f"%cost_1)
print("Cost for entire season -- $%6.2f"%cost_season)

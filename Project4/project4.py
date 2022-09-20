#---------------------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #4
# Due---------October 9,2018
#
# This program calculate statistics concerning the weights
# of newborn bison in an animal science research project.
# The user will enter the weight in pounds for each of
# several bison in the study. Any negative number will
# serve as a sentinel to mark the end of the input. The
# program will calculate and display the average weight of
# the bison. It will also count the bison in each of three
# size categories: small,medium, and large. In addition to
# the average weight and the category counts, it will
# compute and print the weight of the heaviest bison in the study.
#---------------------------------------------------------------------
print("Bison weights")
print("-------------")
print()

total=0
count=0
small=0
medium=0
large=0
weight_list=[]
weight=float(input("Weight #1: "))

while weight >= 0:
    count=count+1
    total=total+weight
    weight_list.append(weight)
    if weight < 40.0:
        small=small+1
    if weight >= 40.0 and weight <= 50.0:
        medium=medium+1
    if weight > 50.0:
        large=large+1
    weight=float(input("Weight #{}: ".format(count+1)))

print()
average=total/count
print("Average weight: %0.1f"%average)
print()
print("Small bison : %d"%small)
print("Medium bison: %d"%medium)
print("Large bison : %d"%large)
print()
print("Heaviest bison:",max(weight_list))

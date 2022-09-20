#--------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #8
# Due---------November 28,2018
#
# This program uses the distance function to compute and
# print the results of a stone slung from a slingshot
# to try and hit a pig a certain distance away.
#--------------------------------------------------------


# ---------------------------------------------------------
# Factorial Function; For Sine Function
# ---------------------------------------------------------

def fact(n):
    factorial = 1
    count = 2
    while count <= n:
        factorial *= count
        count += 1
    return factorial

# ---------------------------------------------------------
# Sine Function; For Distance Function
# ---------------------------------------------------------

def sin(x,n):
    sine = 0
    for count in range(n+1):
        sign = (-1)**count
        sine += sign*((x**((2*count)+1))/(fact((2*count)+1)))
    return sine

# ---------------------------------------------------------
# Distance Function
# ---------------------------------------------------------

def dist(draw,angle):
    velocity = draw * 10
    g = 32.2
    pi = 22/7
    radians = angle * (pi/180)
    distance = ((velocity**2)*sin(2*radians,20))/g
    return distance

# ---------------------------------------------------------
# Result Function
# ---------------------------------------------------------

def res(far,distance):
    under = far - 2
    over = far + 2
    if distance >= under and distance <= over:
        result = "Result of shot ---------------- OINK!!"
    elif distance > over:
        off = abs(over - distance)
        result = "Result of shot ---------------- %d feet too long"%off
    elif distance < under:
        off = under - distance
        result = "Result of shot ---------------- %d feet too short"%off
    return result

# ---------------------------------------------------------
# ______________________MAIN PROGRAM_______________________
# ---------------------------------------------------------

far = int(input("Distance to pig (feet) -------- "))
print()

elevation = float(input("Angle of elevation (degrees) -- "))
length = float(input("Draw length (inches) ---------- "))
print()

end = res(far,dist(length,elevation))
print(end)
while end != "Result of shot ---------------- OINK!!":
    print()
    elevation = float(input("Angle of elevation (degrees) -- "))
    length = float(input("Draw length (inches) ---------- "))
    print()
    end = res(far,dist(length,elevation))
    print(end)
    

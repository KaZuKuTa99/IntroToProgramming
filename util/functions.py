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
# Factorial using for-loop (WORKS)
# ----------------------------------------------------
def fact(n):
    factorial = 1
    for count in range(2,n+1):
        factorial *= count
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
# Taylor series using for-loop;must use fact function
# (WORKS)
# ----------------------------------------------------
def dist(draw,angle):
    velocity = draw * 10
    g = 32.2
    pi = 22/7
    radians = angle * (pi/180)
    distance = ((velocity**2)*sin(2*radians,20))/g
    return distance

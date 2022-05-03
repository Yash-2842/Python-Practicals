import math
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b**2 - (4*a*c)
root1 = (-b + math.sqrt(d))/(2 * a)
root2 = (-b - math.sqrt(d))/(2 * a)

if d == 0:
    print(f"root of quadratic equation is {root1}")
elif d > 0:
    print(f"root1: {root1} \n root2: {root2}")
else:
    print("INVALID INPUTS")

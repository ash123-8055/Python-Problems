import math

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
print(f"The Quadratic Equation is {a}x^2 + {b}x + {c}")

delta = b*b - 4*a*c

root1 = (-b + math.sqrt(delta)) / 2*a
root2 = (-b - math.sqrt(delta)) / 2*a

print(f"The Roots of the Quadratic Equation are {root1} and {root2}")
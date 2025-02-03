import math

def distance(x, y):
    return math.sqrt(x*x + y*y)

x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(f"The Euclidean distance from the point ({x},{y}) to the origin is {distance(x, y)}")
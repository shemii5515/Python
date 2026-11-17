# Lambda functions
square = lambda a: a * a
rectangle = lambda l, b: l * b
triangle = lambda b, h: 0.5 * b * h

# User input
a = float(input("Enter the side of square: "))
print("Area of square =", square(a))

l = float(input("Enter the length of rectangle: "))
b = float(input("Enter the breadth of rectangle: "))
print("Area of rectangle =", rectangle(l, b))

base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
print("Area of triangle =", triangle(base, height))


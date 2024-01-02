radius = float(input("Enter the radius of the circle: "))
pi = 22/7
area_circle = (radius**2)*pi
print("The area of the circle is",area_circle,"square units")


upper_length = float(input("\nEnter the upper length of the trapezoid: "))
lower_length = float(input("Enter the lower length of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
area_trapezoid = (upper_length + lower_length)/2*height
print("The area of the trapezoid is",area_trapezoid,"square units")

base = float(input("\nEnter the base length of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
area_parallelogram = base*height
print("The area of parallelogram is",area_parallelogram,"square units")

diagonal1 = float(input("\nEnter the length of diagonal 1 of rhombus: "))
diagonal2 = float(input("Enter the length of diagonal 2 of rhombus: "))
area_rhombus = diagonal1*diagonal2*0.5
print("The area of rohmbus is",area_rhombus,"square units")

side = float(input("\nEnter the side length of the square: "))
area_square = side**2
print("The area of the square is",area_square,"square units")


#To convert decimal to fraction
from fractions import Fraction
Fraction(3.1416)
str(Fraction(3.1416))

#To convert decimal to ratio
(3.1416).as_integer_ratio()
#π = 3.1416 = 7074254294673575 / 2251799813685248 != 22 / 7

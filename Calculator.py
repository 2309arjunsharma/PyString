d = input("Enter the operation(+,-,*,/,%,//,**): ")
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
if d=="+":
    def addition(a, b):
        return a+b
    addition(a, b)
    print(addition(a, b))
if d=="-":
    def subtraction(a, b):
        return a-b
    subtraction(a, b)
    print(subtraction(a, b))
if d=="*":
    def multiplication(a, b):
        return a*b
    multiplication(a, b)
    print(multiplication(a, b))
if d=="/":
    def division(a, b):
        return a/b
    division(a, b)
    print(division(a, b))
if d=="%":
    def remainder(a, b):
        return a%b
    remainder(a, b)
    print(remainder(a, b))
if d=="//":
    def divi(a, b):
        return a//b
    divi(a, b)
    print(divi(a, b))
if d=="**":
    def exponent(a, b):
        return a**b
    exponent(a, b)
    print(exponent(a, b))


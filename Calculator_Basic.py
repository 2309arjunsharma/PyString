print("Welcome to Arjun's calculator!!!")
print("\nEnter 2 numbers to start")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
x = min(num1,num2)
y = max(num2,num1)
operations = input("Enter an operation to do(+,-,*,/,**,//,%): ")
if operations=="+":
    print(y+x)
elif operations=="-":
    print(y-x)
elif operations=="*":
    print(y*x)
elif operations=="/":
    print(y/x)
elif operations=="**":
    print(y**x)
elif operations=="//":
    print(y//x)
else:
    print(y%x)

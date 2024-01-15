num = int(input("Enter a number: "))
if num%5==0:
    print("Divisible by 5")
elif num%6==0:
    print("Divisible by 6")
elif num%7==0:
    print("Divisible by 7")
else:
    print("Number is not divisible by 5, 6 or 7")




n = int(input("Enter a number: "))
if n%5==0 or n%6==0 or n%7==0:
    print("Number is divisible by 5, 6 or 7")
else:
    print("Number is not divisible by 5, 6 or 7")

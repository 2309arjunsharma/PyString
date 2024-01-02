a = str(input("Enter your name: "))
b = int(input("Enter your age: "))
if(b<18):
    c = int(input("Enter your class: "))
    d = str(input("Enter your school name: "))
    print("\nName is",a)
    print("\nAge of",a,"is",b)
    print("\nSchool name of",a,"is",d)
    print("\nClass of",a,"is",c)
else:
    e = str(input("Enter your profession: "))
    print("\nName is",a)
    print("\nAge is",b)
    print("\nWork done by",a,"is",e)
    

if(b<=1):
    print(a,"is an infant")
elif(b>1 and b<13):
    print(a,"is a child")
elif(b>12 and b<18):
    print(a,"is a teenager")
elif(b>17 and b<65):
    print(a,"is an adult")
else:
    if(b>65 and b<=100):
        print(a,"is an elderly person")
    else:
        print(a,"is more than 100 years")

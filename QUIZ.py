a = "Quiz on earth"
a = a.upper()
print(a)
point = 0
print("\nYou have",point,"points and there are 10 questions")

print("\nQ1")
b = str(input("Which is the biggest country based on population: "))
if(b=="India"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(b!="India"):
        print("Try again")
        b = str(input("Which is the biggest country based on population: "))
        if(b=="India"):
            print("You are correct")
            print("Let's move to the next question")
            point = point + 1
            print("You got",point,"point")
            break

print("\nQ2")
c = str(input("Which is the highest mountain on Earth: "))
if(c=="Mt.Everest" or c=="Mount Everest"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(c!="Mt.Everest" or c=="Mount Everest"):
        print("Try again")
        c = str(input("Which is the highest mountain on Earth: "))
        if(c=="Mt.Everest" or c=="Mount Everest"):
            print("You are correct")
            print("Let's move to the next question")
            point = point + 1
            print("You got",point,"points")
            break
print("\nQ3")
d = str(input("Which is deepest point on Earth: "))
if(d=="Mariana Trench"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(d!="Mariana Trench"):
        print("Try again")
        d = str(input("Which is the highest mountain on Earth: "))
        if(d=="Mariana Trench"):
            print("You are correct")
            print("Let's move to the next question")
            point = point + 1
            print("You got",point,"points")
            break

a = "Quiz on earth"
a = a.upper()
print(a)
point = 0
print("\nYou have",point,"points and there are 10 questions")

print("\nQ1")
b = str(input("Which is the biggest country based on population?\n"))
if(b=="India"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(b!="India"):
        print("Try again\n")
        b = str(input("Which is the biggest country based on population?\n "))
        if(b=="India"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"point")
            break

print("\nQ2")
c = str(input("Which is the highest mountain on Earth?\n"))
if(c=="Mt.Everest" or c=="Mount Everest"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(c!="Mt.Everest" or c!="Mount Everest"):
        print("Try again\n")
        c = str(input("Which is the highest mountain on Earth?\n"))
        if(c=="Mt.Everest" or c=="Mount Everest"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break
print("\nQ3")
d = str(input("Which is deepest point on Earth?\n"))
if(d=="Mariana Trench"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(d!="Mariana Trench"):
        print("Try again\n")
        d = str(input("Which is deepest point on Earth?\n"))
        if(d=="Mariana Trench"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break

print("\nQ4")
e = str(input("What is equator?\n"))
if(e=="It is a line of latitude of 0 degrees that runs through the centre of the Earth and divides it into 2 equal halves."):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(e!="It is a line of latitude of 0 degrees that runs through the centre of the Earth and divides it into 2 equal halves."):
        print("Try again\n")
        e = str(input("What is equator?\n"))
        if(e=="It is a line of latitude of 0 degrees that runs through the centre of the Earth and divides it into 2 equal halves."):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break

print("\nQ5")
f = str(input("Which lake is the largest?\n"))
if(f=="Caspian Sea"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(f!="Caspian Sea"):
        print("Try again\n")
        f = str(input("Which lake is the largest?\n"))
        if(f=="Caspian Sea"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break

print("\nQ6")
g = str(input("Which is the largest country based on land?\n"))
if(g=="Russia"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(g!="Russia"):
        print("Try again\n")
        g = str(input("Which is the largest country based on land?\n"))
        if(g=="Russia"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break

print("\nQ7")
h = str(input("Which city is the oldest?\n"))
if(h=="Damascus"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(h!="Damascus"):
        print("Try again\n")
        h = str(input("Which city is the oldest?\n"))
        if(h=="Damascus"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break
print("\nQ8")
i = str(input("Which is the most active volcano and where is it?\n"))
if(i=="Kilauea in Hawaii, USA"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(i!="Kilauea in Hawaii, USA"):
        print("Try again\n")
        i = str(input("Which is the most active volcano and where is it?\n"))
        if(i=="Kilauea in Hawaii, USA"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break


print("\nQ9")
j = str(input("What is the population on Earth?\n"))
if(j=="8.1 Billion"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(j!="8.1 Billion"):
        print("Try again\n")
        j = str(input("What is the population on Earth?\n"))
        if(j=="8.1 Billion"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break


print("\nQ10")
k = str(input("Which is the lowest point on Earth?\n"))
if(k=="Dead Sea"):
    print("You are correct")
    print("Let's move to the next question")
    point = point + 2
    print("You got",point,"points")
else:
    while(k!="Dead Sea"):
        print("Try again\n")
        k = str(input("Whis the lowest point on Earth?\n"))
        if(k=="Dead Sea"):
            print("You are correct")
            print("Let's move to the next question")
            point = point - 1
            print("You got",point,"points")
            break
total = 20
print("\nThank you for attempting the Earth quiz!")
print("You got",point,"points out of",total)
print("\nYour result:")
if(point==20):
    print("\nExcellent")
elif(point>=17 and point<20):
    print("\nVery Good")
elif(point<17 and point>=13):
    print("\nGood")
elif(point<13 and point>=10):
    print("\nAverage")
else:
    print("\nMust work hard!")




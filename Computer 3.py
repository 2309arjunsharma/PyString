
a = float(input("Enter marks in English:"))
b = float(input("Enter marks in Hindi:"))
c = float(input("Enter marks in Maths:"))
d = float(input("Enter marks in Science:"))
e = float(input("Enter marks in SST:"))
avg = (a+b+c+d+e)/5
print("Average is",avg)
if(avg>=80):
    print("Student is a scholar")
else:
    print("Student is not a scholar")



#marks["95", "96", "97", "98", "99"]
i = 0
total = 0
for i in range(12):
    a = float(input("Enter marks:"))
    total = total + a
    i = i + 1
    if i == 6:
        break
print(total)
print(i)
print(total/i)
    


txt = "  Arjun Sharma  "
print(txt.upper())
print(txt.strip().upper())
print(len(txt))
print(txt.replace("A", "a"))
txt = txt.strip().replace("A", "a")
x = len(txt)
print(x)
i = 0
while(i<x):
    print(i)
    print(txt[i].upper()) 
    i = i + 1

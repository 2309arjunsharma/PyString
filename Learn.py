fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)
fruits[0] = "kiwi"
print(fruits)
fruits.insert(1,"pineapple")
print(fruits)
fruits.remove("banana")
print(fruits)
print(fruits[-2])
fruits.append("mango")
fruits.append("melon")
fruits.insert(1,"apple")
fruits.insert(2,"banana")
print(fruits[2:5])
print(fruits*3)
print(len(fruits))
if "kiwi" in fruits:
    print("Kiwi is a fruit")
else:
    print("Kiwi is a vegetable")

set_fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
set_fruits.update(more_fruits)
print(set_fruits)

def my_function():
    print("Hello from a function")

my_function()



def my_function(x):
    return x + 5

print("Enter X : ", my_function(3))



def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function(*kids)

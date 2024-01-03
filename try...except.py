try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


try:
  print(x)
except:
  print("An exception occurred")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")


try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

y = -1

if y < 0:
  raise Exception("Sorry, no numbers below zero")


a = "hello"

if not type(a) is int:
  raise TypeError("Only integers are allowed")


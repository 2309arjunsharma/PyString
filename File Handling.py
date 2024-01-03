f = open("C:\\PythonWorkspace\\SchoolAssignment\\Enrichment Activity 1.py", "r")

#print(f.read())
print(f.read(10))
print(f.readline())

for x in f:
  print(x)

f = open("C:\\PythonWorkspace\\SchoolAssignment\\Enrichment Activity 1.py", "a")
f.write("Now the file has more content!")


#open and read the file after the appending:
f = open("C:\\PythonWorkspace\\SchoolAssignment\\Enrichment Activity 1.py", "r")
print(f.read())

f.close()

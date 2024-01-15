password = input("Enter password: ")
i = 0
if password == "pass123":
    print("\nPassword was correct!\tAccess Granted")
else:
    while password != "pass123":
        print("Wrong!")
        password = input("Enter password again: ")
        i = i + 1
        if(i==5):
            print("This device is locked")
            break


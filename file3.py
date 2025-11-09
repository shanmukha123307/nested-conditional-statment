age=int(input("enter your age:"))
if age>=10 and age<=20:
    print("you are allowed:)")
else:
    if age>20:
        print("you are too old to be in my class")
    else:
        if age<10:
            print("you are too young to be in my class")
        else:
            print("invalid input :(")
medical_cause=input("do you have medical cause Y or N:")
a=int(input("enter the atendence:"))
if medical_cause=="Y":
    print("you are allowed")
else:
    if a>=75:
        print("allowed")
    else:
        print("not allowed ")
        
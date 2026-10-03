Hurricane_Sp=float(input("What is the current speed of the hurricane? (enter in mph)"))

if Hurricane_Sp >=157:
    print("You are experiencing a level 5 hurricane! DANGER PLEASE SEEK HELP!")
elif Hurricane_Sp in range(130,157):
    print("You are experiencing a level 4 hurricane! Please Evacuate!")
elif Hurricane_Sp in range(111,129):
    print("You are experiencing a level 3 hurricane!")
elif Hurricane_Sp in range(96,110):
    print("You are experiencing a level 2 hurricane.")
elif Hurricane_Sp in range(74,96):
    print("You are experiencing a level 1 hurricane.")
else:
    print("You are not experiencing a hurricane, please try again later.")


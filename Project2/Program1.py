user_num=float(input("What number would you like to operate on?"))
user_op=input("What function would you like to perform? (+ - * / 2 R)").upper()

if user_op=="+":
    user_num2=float(input("What number would you like to add?"))
    print(f"Your solution is {user_num+user_num2}!")
elif user_op=="-":
    user_num2=float(input("What number would you like to subtract"))
    print(f"Your solution is {user_num-user_num2}!")
elif user_op=="*":
    user_num2=float(input("What number would you like to multiply by?"))
    print(f"Your solution is {user_num*user_num2}!")
elif user_op=="/":
    user_num2=float(input("What number would you like to divide by?"))
    print(f"Your solution is {user_num/user_num2}!")
elif user_op=="2":
    print(f"Your solution is {user_num**2}!")
elif user_op=="R":
    print(f"Your solution is {user_num**0.5}!")
else:
    print("Invalid Character")

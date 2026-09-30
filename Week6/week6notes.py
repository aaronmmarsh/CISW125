signal_color = input("enter the color of the light")
is_blinking = input("Is the light blinking?")
if signal_color =="red":
    if is_blinking == "yes":
        print("This is a four way stop")
    else:
        print("Stop")

#Login Program

username = input("What is your username?")
password = input("What is your password?")

if username == 'admin':
    if password=='cat:':
        print("Login successful")
    else:
        print('Password is incorrect')
else:
    print("username is incorrect")

#Discount based on total amount

total_amount=float(input("what was your total"))
is_member=input("are you a member?")


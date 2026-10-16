secret_num=68

user_guess=int(input("Pick a number 1-100: "))

while user_guess<100 and user_guess!=secret_num:
    user_guess=int(input("Inncorrect Number guess again!:"))
print("Thats right!")
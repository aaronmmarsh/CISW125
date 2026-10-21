# Intro to Programming
# Debug Exercise 3
#
# There are two problems here. One is quite obvious;
# the other is less so. If you need a hint
# send me a message on Canvas or email me ~Tom

while True:
    # This loop should output numbers from 1 through 10.
    print("Counting up: ", end=" ")
    for count in range(1, 11): #This needed to be changed to an 11 because it goes up until 10 and doesnt include it.
        print(count, end=" ")
    print("") # this is just an easy way to make a new-line and makes it much more readable
    choice = input("Should I print them again? (y/n)")
    if choice.lower() == 'n':
        break #just added break to break the loop and stop it from asking
        # do something to stop the loop
print("Okay!")

#What is a loop?
#A loop repeats code

#Repeat this loop 3 times

# for number in range(3):
#     #Print hello each time the loop runs
#     print("Hello")


#While loops
# A While loop repeats while a condition is TRUE

#Make a program that is going to print 1 through 5

#Create a variable starting at 1

# num = 1

# while num<=5:
#     print(num)
#     num+=1

#I want to start counting at zero, count to fifty, and get there by increments of 5

# number=0
# while number<=50:
# #     print(number)
# #     number+=5

# #While loop is useful when you want to keep asking until the user give you a valid  answer
# #Ask the user for their Age
# # age=int(input("What is your age? >"))
# # #Keep looping if the age is less than one or greater than 120
# # while age <1 or age>120:
# #     #Tell the user invalid input
# #     print("Invalid Age!")

# #     #ask the user to enter their age again
# #     age=int(input("What is your age? >"))
# # print("Thank you!")

# #For Loop
# #A for loop works through items one at a time

# #Create a list containing 3 games
# cars=["Bmw", 'ford', 'chevy']
# games=["Minecraft", "Mario", "Zelda"]
# #Take one item from the games list at a time
# for game in games:
#     #Print the current game
#     print(game)
#     #Each time the loop repeats, game holds the next item on the list

# for i in cars:
#     print(i)

# #Range() creates a sequence of numbers
# #Starts at two and stops right before 8

# for number in range(2,8):
#     print(number)
# #Remember: The ending number is range() is not included

# #we  can also  perform calculations within the loop
# #Loop through numbers 2 and 7

# for number in range(2,8):
#     #multiply the number by itself
#     square=number*number
#     print(square)

#Looping through a string
# #Store a name inside of a string 
# name="Aaron"
# #Take one character from the string at a time
# for letter in name:
#     print(letter)


# #Using Break
# #Break stops a loop early

# #Loop through numbers one through ten
# for numbers in range(1, 11):
#     print(numbers)
#     if numbers==5:
#         break

#Nested Loop is a loop inside another loop

#Outer Loop is going to run through 1,2,3

# for number in range(1,4):
#     #inner loop also runs though 1,2,3
#     for number2 in range(1,4):
#         print(number,number2)

#Using a while loop when repitition depends on a condition
#Keep looping while an answer is not yes

while answer !='yes':
    answer=input('answer yes!')

#Use a for loop when working through items
#Go through each item in the list
item=["apples", "orange", "kiwis"]
for items in item:
    print (item)

    

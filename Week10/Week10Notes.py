#Week 10 function notes
#A function is a named set of instructions you can run whenever you want
#Functions let us write code once and reuse it

#Define a function: Create a function in Python using 'def'
#Call a function: running a function by using its name with parentheses
#Parameter: A placeholder variable inside the function definition
#Argrument: The real value you pass in when you call the function

#Define (create)
# def say_hello():
#     print("hello")

# #call the function
# say_hello()

# #Arguments and Parameters
# #Function that is going to greet me by name

# def greet(name):
#     print(f"Hello, {name}!")
# #Call the function and it will say "Hello, Aaron!"
# #An argument is a real value, Sebastian the agrument in the function below
# #Parameters are like blanks, Arguments fill them in
# greet("Aaron")

#Why are functions useful?
#Reusing code (Don't have to copy and paste blocks of code)
#Organization, allows our program to become more readable
#Breaking Big Problems into smaller parts

# def show_menu():
#     print("Welcome")
#     print("Pick an option......")
#     print("Goodbye")

# show_menu()

#Print vs Return
#A function that prints
# def hello_world():
#     print("hello")
# #This shows the text to the user but it doesnt give a value back to the rest of the program

# #A function that returns
# def hello():
#     return "hello world"
# #This sends a value back to whereever the function is called, it can be stored, used, printed, etc
# #Print is for the user, Return is for the program
# hello()
# hello_world()

#Calc  function that uses two parameters, and will have if/elif based on the operator
def Calc(num1,num2):
    operator=input("Choose an operation: +,-,/,*")
#use if/elif to decide what to do
#perform the math
#Print or return the result

#Fake loop, a function calling itself
#A function can call itself, its called recurrsion
#Behaves like a loop it repeats until a condition is met

def Play_again():
    #want user to be prompted with question if then say y then reprompt. if n break out of the loop
    question=input("do you want to play again? y/n").lower()
    if question=="y":
        Play_again()
    else:
        print("Goodbye")
        
Play_again()
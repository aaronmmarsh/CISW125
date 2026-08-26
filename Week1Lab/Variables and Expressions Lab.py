# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.
GGame="Overwatch"
BadGame="Dark Souls"
OldGame="SMG2"
# Then print your variables.
print(GGame,BadGame,OldGame)
# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
BadGame="Not Dark Souls"
# After you've done this, try to print your variables in string using f-strings.
print(f"my favorite game currently has to be{GGame} I've been grinding ranked for so  long  :,)")
print(f"I have a hatred for {BadGame}, and most souls-likes. I'm just bad ig")
print(f"but my all time favorite has to be{OldGame} such a classic")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
a=5+5
s=10-3
m=5*5
d=5/2
# Store the results of your expressions in a variable and then print the outcome
print(a,s,m,d)

# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp


# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
fname="Aaron"
lname="Marsh"
fullname=fname+lname
print(fullname)

# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)
x=5
varequation=x+3
print(varequation)

# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
c=0
f=c*9/5+32

print(f)
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.

# Upload this to Canvas under the Variable and Expressions Lab assignment.

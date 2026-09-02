#Whats the difference between int and float?
#Int is whole numbers (10,2,5,7)
#Float contains decimals (1.5, 10.7)


# x=15
# y=6

# print(x,type(x))
# print(y,type(y))

# print(x//y) #whole number value, floor division
# print(x/y) # regular division, will give the float

# user_text=input("type something!") #user input auto converts any response to string text
# print(f"hello, {user_text}")

# user_age=input("Give me your age:")
# age_int=int(user_age)
# print(age_int, type(age_int))

# word="Python"
# print(word[0])
# print(word[1])

# print(word[0:3])
#start:end means start and stop before end [start:end] goes up to a character but not including

#built in python functions
#.upper(), this converts string to all uppercase
#.lower(), this converts string to all lowercase

# phrase="Hello World"
# print(phrase.upper())
# print(phrase.lower())

fruits=["apple", "banana","orange"]
numbers=[10.5, 3]
mixed=[100,"score",3.5]

print(fruits)
print(mixed)

print(fruits[0])
print(fruits[0:2])

#to add to a list we append the list name
fruits.append("Kiwi")
print(fruits)

user_fruit=input("whats your favorite fruit?:")
fruits.append(user_fruit)
print(fruits)
x=10
y=5.5
print(x,y)

# #You can still do math with both a float and integer

x=input("Give me a whole number:")
y=input("Now give me a number with a decimal:")
print(x,y)

# # A string is a data type

text="hmmm"
okay="okay"+text
print(okay)
print(okay[0:4])

# A list can contain any type of data!

car_brand=["Toyota","Chevy","BMW"]
car_brand.append("Ford")
print(car_brand)
car_brand.remove("Chevy")
print(car_brand)
print(len(car_brand))

#I learned about different applications for built in functions in python. I could use the ability to differenciate between different
#data types to potentially weed out inputs I dont want from a user. For example if I was building a calculator and I didn't want the
#user to input any str values I could have the terminal show an error message if given any str value. I was also thinking about how
#would go about auto formating some text given to me by the user using the .lower() and .upper() functions. Overall this was a very
#Interesting and fun subject to learn about.
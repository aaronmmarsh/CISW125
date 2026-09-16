#What is a boolean?
#A boolean value is true or false



#answer=input("Do you want to continue? (Y/N)").upper()
#if answer == "Y":
#    print("Continuing the Program!")
#elif answer == "N":
#    print("Okay, exiting now.")
#else:
#    print("Error!")

#Comparison Operators
# == equal to  
# < greater than
# > less than
# >= greater than or equal to
# <= less than or equal to
# != not equal to

#score=85
#print(score==100)
#print(score!=85)

#How do we compare 3 values?
#We can compare three or more values with "and" & "or"

#temp=72
#if temp >= 68 and temp <= 75:
#    print("Comfy Temps :)")

#When using "and" both conditions must be true
#when using "or" one condition must be true

day="Saturday"
is_holiday=False
if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You don't have class today")

#I want to print "You dont have class today?"

score=75
if score <= score <90:   #score >= 60 and score < 90:
    print("Mediocre Grade")

#Give me a conditional program that prints out shipping cost depending on total price.

price=float(input("Whats the cost of your package?"))
if price<25:
    print("Shipping is $10")
elif price<50:
    print("Shipping is $7.99")
else:
    print("Shipping is Free!")

list1=[1,2,3]
list2=[1,2,3]
list3=list1

print(list1==list2)
print(list1 is list2)
print(list1 is list3)

#== compares values of the content
# "is" compares the identity

#learn how to write, read and edit files using python
#Common modes when using files

# 'r' read only
# you can read this file but not change it
#Error if file doesn't exist

# 'w' write
# Create the file if it doesnt exist
# Overwrites the file if it already exists

# 'a' append
# Creates the file if it doesn't exist 
# Adds new text to the file, does not delete existing data

#with open("FolderName/FileName", "Mode")
# with open("Week9/stuff.txt", "r") as file:
#     contents=file.read()
#     print(contents)

#I want to overwrite the content of stuff.txt

# with open("Week9/stuff.txt", "w") as file:
#     file.write("Hello!\nThis Line appears underneath")
#Once we leave the indentation block the file automatically closes

#Reading from a file
#Method A: Read the whole file at once
# with open("Week9/stuff.txt", "r") as file:
#     contents=file.read()
#     print(contents)


# #Method B: Read line by line using a for loop 
# with open("Week9/stuff.txt", "r") as file:
#     for line in file:
#         print(file)

#Appending to a file (Adding to a file)
#Appending adds to the end of a file without deleting whats already there
# with open("Week9/stuff.txt", "a") as file:
#     file.write("\nThis should appear at the very end, because we used mode a")


username=input("Set your username:")
password=input("Set your password:")

with open("Project4/logininfo.txt", "w") as file:
    file.write(f"Username: {username}\nPassword: {password}")
    
def login():
    nameinp=input("Username:")
    passwordinp=input("Password:")
    if nameinp==username and password==passwordinp:
        print("Login Successful!")
    else:
        print("Access Denied.")
        login()
        
login()


    
    

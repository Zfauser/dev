# Simple login program in python3
# Save login
def login():
    print("Login")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "admin":
        print("Login successful")
    else:
        print("Login failed")
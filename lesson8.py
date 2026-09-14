username = input("Enter your username: ").lower()
if username == "admin" or username == "root":
    print("Access granted")
else:
    print("Access denied")

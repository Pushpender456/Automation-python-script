IP = input("Enter Your IP Address : ")
Role = input("Enter Your Role : ").strip().capitalize()

if Role == "Admin":
    print("Access Granted: Welcome to the Secure Network!")
elif Role == "Guest":
    print("Limited Access: You can only view public pages.")
else:
    print("Access Denied: Unknown Role!")        
# Login Function
"""
Write a login fun which accepts the user only when the user name and password are same , 
and displays a message login successfull, 
otherwise it keeps asking the user to enter the credentials untill they are correct
"""




def login():
    while True:
        userName = input("Enter the User Name: ")
        password = input("Enter the Password :")
        if userName == password:
            print("Login Successfull")
            break
        else:
            print("Incorrect Credentials")
            print("Please enter the correct credentials")
        

login()
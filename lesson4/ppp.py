password = "001122"
pswrd = input()
while pswrd != password:
    print("Incorrect password")
    pswrd = input()
    if pswrd == password:
        print("Welcome to system!")
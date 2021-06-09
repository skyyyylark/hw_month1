# age = [19, 25, 13, 90]
# age[0] = 20
# age2 = (19, 25, 13, 90)
# age3 = []
# print(age)
# print(age2)
# print(age[0:2])
# print(age2[0:2])
#
# for i in range(10):
#     age = int(input())
#     age3.append(age)
# print(age3)

# names = []
# for i in range(4):
#     name = input()
#     names.append(name)
# print(names)


# password = input()
# while len(password) < 8:
#     print("Password error!")
#     password = input()


pw = "0550955601"
password = input()
while password == pw:
    print("Incorrect password")
    password = input()

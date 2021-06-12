import random

num = random.randint(1, 15)

print(num)

guess = int(input())

while num != guess:

    if num - 2 <= guess <= num + 2:
        print("Горячо!")
    elif num - 4 <= guess <= num + 4:
        print("Тепло!")
    else:
        print("Холодно")

    guess = int(input())
print("Well done!")
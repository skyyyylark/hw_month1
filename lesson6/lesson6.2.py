def real_age(text):
    while True:
        age = input(text)
        try:
            age = int(age)
            break
        except Exception:
            pass
    print(age)
real_age("Enter your age: ")

eng_rus = {
    "car" : "машина",
    "cat" : "кошка",
    "dog" : "собака",
    "table" : "стол"
}

rus_eng = {
    "машина" : "car",
    "кошка" : "cat",
    "собака" : "dog",
    "стол" : "table"
}


while True:
    lang = input("Введите язык (eng/rus): ")
    same_eng = eng_rus.keys()
    same_rus = rus_eng.keys()
    if lang == "eng":
        word = input("Введите слово для перевода: ")
        try:
            print(f"Перевод введенного слова: {eng_rus[word]}")
        except KeyError:
            if word in same_rus:
                print(f"Это слово есть в другом словаре! {rus_eng[word]}")
            elif word not in same_rus:
                print("Этого слова нет ни в одном из словарей, хотите добавить? (Yes/No)")
                opt = input()
                if opt == "Yes":
                    eng_rus[word] = input(f"Перевод для слова {word} -")
                else:
                    pass
    elif lang == "rus":
        word = input("Введите слово для перевода: ")
        try:
            print(f"Перевод введенного слова: {rus_eng[word]}")
        except KeyError:
            if word in same_eng:
                print(f"Это слово есть в другом словаре! {eng_rus[word]}")
            elif word not in same_eng:
                print("Этого слова нет ни в одном из словарей, хотите добавить? (Yes/No)")
                opt = input()
                if opt == "Yes":
                    rus_eng[word] = input(f"Перевод для слова {word} -")
                else:
                    pass

    else:
        break

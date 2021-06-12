def translate(dictionary):
    a = input("Введите слово для превода: ")
    try:
        print(f"Перевод введенного слова: {dictionary[a]}")
    except KeyError:
        same_en, same_ru = eng_rus.keys(), rus_eng.keys()
        if a in same_ru:
            print(f"Это слово есть в другом словаре: {eng_rus[a]}")
        else:
            print("Такого слова в словаре нет! Хотите добавить? ")
            option = input()
            if option == "yes":
                dictionary[a] = input(f"Перевод для слова {a} - ")
            else:
                pass


eng_rus = {
    "dog" : "собака",
    "cat" : "кошка",
    "pet" : "питомец",
    "table" : "стол",
    "simple" : "простой"
}

rus_eng = {
    "собака" : "dog",
    "кошка" : "cat",
    "питомец" : "pet",
    "стол" : "table",
    "простой" : "simple"
}
lang = input("Введите язык: ")
while True:
    if lang == "eng":
        translate(eng_rus)

    elif lang == "rus":
        translate(rus_eng)


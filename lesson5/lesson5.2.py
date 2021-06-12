d = {
    "pet": ["питомец", "любимец"],
    "fly": ["сущ - муха", "гл - летать"]
}
word = d["fly"]
for i in range(len(word)):
    print(f"Значение {i+1} : {word[i]}")
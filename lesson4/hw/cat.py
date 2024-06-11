# 4. Пользователь вводит текст. В тексте есть слово "cat", надо начиная с него вывести текст до конца:
# Ввод:  "The was a cat at backyard" " Do you know the story about the fat cat?
# "What is the fat cat doing in the cabin right now?"
# Вывод: "cat at backyard"


text = input("Введите текст: ")


index_cat = text.find("cat")

if "cat" in text:
    result = text[index_cat:]
    print(result)
else:
    print("Слово 'cat' не найдено в тексте.")

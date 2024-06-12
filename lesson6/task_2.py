a = "There are available many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."
# 1. Найти кол-во слов в тексте
print(a.count(" ") + 1)
print(len(a.split()))

# 2. Найти сколько раз встречается слово "you" в тексте
print(a.count("you"))
# print(a.find("you")) находит индекс

# 3. Сколько раз встречается каждое слово?
words_count = {}
a_cleared = a
for symbol in a_cleared:
    if not symbol.isalpha() and symbol not in [" ", "-"] :
        a_cleared = a_cleared.replace(symbol, "")

print(a_cleared)

words = a_cleared.split()
for word in words:
    words_count[word] = a_cleared.count(word)

# 4. Улучшить отображение:
# слово_x      6
# слово_y      3
# ...
# print(words_count)
for word, qty in words_count.items():
    print(f"{word} \t \t {qty}")

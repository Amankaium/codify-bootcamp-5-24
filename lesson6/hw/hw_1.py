a = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."

# Получить словарь, где ключ - то сколько раз слово встречается в
# тексте, а значение - список слов, например:
# {5: ["Lorem", "Ipsum", "as"], 2: ["you", "Internet"], ...

# 3. Сколько раз встречается каждое слово?
words_count = {}
a_cleared = a
for symbol in a_cleared:
    if not symbol.isalpha() and symbol not in [" ", "-"] :
        a_cleared = a_cleared.replace(symbol, "")

# print(a_cleared)

words = a_cleared.split()
for word in words:
    qty = 0
    for check_word in words:
        if check_word == word:
            qty += 1
    words_count[word] = qty

# {"on": 2, "Ipsum": 5, "Lorem": 5, ... }
#   V
# {5: ["Lorem", "Ipsum", "as"], 2: ["you", "Internet"], ...

word_stat = {}
for word, qty in words_count.items():
    # qty = words_count[word] # v
    if qty in word_stat:
        word_stat[qty].append(word)
    else:
        word_stat[qty] = [word]

print(word_stat)

text = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."

cleared_text = text.replace(",", "").replace(".", "")
splitted_text = cleared_text.split()

counter = {}

for word in splitted_text:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
print(counter)

dictionary = {}

for word, qty in counter.items():
    if qty in dictionary:
        dictionary[qty].append(word)
    else:
        dictionary[qty] = [word]

for qty, word in dictionary.items():
    print(f"{qty} \t {word}")





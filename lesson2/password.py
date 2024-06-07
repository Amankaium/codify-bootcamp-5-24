my_pass = "Wiskas123&"
# Поставьте лимит 3-х попыток

i = 0
while i < 3:
    input_pass = input("Введите пароль: ")
    if input_pass == my_pass:
        print("welcome!")
        break
    print("wrong, try again...")
    i += 1
    if i == 3:
        print("Вы исчерпали 3 попытки")
print("end program")

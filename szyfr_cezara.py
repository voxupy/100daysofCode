import string


letters = string.ascii_lowercase
char_list = []

for char in letters:
    char_list.append(char)


word = input("Podaj słowo: ")
encryption = input("Podaj enkrypcje: (1-9) ")


word_list = []

for char in word:
    word_list.append(char)


for item in word_list:
    print(item)
    if item in char_list:
        print(char_list[item])
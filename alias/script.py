# -*- coding: utf-8 -*-

children_dictionary = './resource/words.txt'

def read_file(file):
    with open(file, "r", encoding="utf8") as f:
        return [x.strip() for x in f]

def save_file(file, lst):
    with open(file, "w", encoding="utf8") as f:
        for word in lst:
            print(word, file=f)



if __name__ == '__main__':
    added_words = 0
    lst = set(read_file(children_dictionary))
    exit_repl = ["q", "Q", "Й", "й"]
    while True:
        last_len = len(lst)
        word = input("введите слово >>>\n")
        if word in exit_repl: # выход
            print("было добавлено - {}".format(added_words))
            print("всего слов - {}".format(len(lst)))
            save_file(children_dictionary, lst)
            break

        lst.add(word)
        if last_len != len(lst):
            added_words += 1
            print("слово добавлено")
        else:
            print("такое слово уже есть")



# -*- coding: utf-8 -*-

f = './resource/words.txt'

def read_file(file):
    with open(file, "r", encoding="utf8") as f:
        return [x.strip() for x in f]

def save_file(file, lst):
    with open(file, "w", encoding="utf8") as f:
        for word in lst:
            print(word, file=f)

if __name__ == '__main__':
    pass
    lst = set(read_file(f))
    exit_repl = ["q", "Q", "Й", "й"]
    while True:
        last_len = len(lst)
        word = input("введите слово >>>\n")
        if word in exit_repl: # выход
            save_file(f, lst)
            break

        lst.add(word)
        if last_len != len(lst):
            print("слово добавлено")
        else:
            print("такое слово уже есть")



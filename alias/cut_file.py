
"разбивает текстовый файл на несколько файлов"

import os


f = './resource/children_dictionary.txt'
target_direct = './resource/target_children'
sep_num = 8

def read_file(file):
    with open(file, "r", encoding="utf8") as f:
        return [x.strip() for x in f]

def save_file(file, lst):
    with open(file, "w", encoding="utf8") as f:
        for word in lst:
            print(word, file=f)


def group(iterable, count):
    """ Группировка элементов последовательности по count элементов """

    return list(zip(*[iter(iterable)] * count))

l=[1,2,3,4,5,6,7]

def cut_2(iterable, count):
    return lambda n: map(None, *[iter(iterable)]*count)

def partition(lst,siz):
    """Разбиение списка на куски равной длины размером siz"""
    return [lst[i:i+siz] for i in range(0,len(lst),siz)]


def enumerate_words(word_groups):
    res_groups = []
    for group in word_groups:
        res_group = []
        for n, word in enumerate(group, start=1):
            res = "{}. {}".format(n, word)
            res_group.append(res)
        res_groups.append(res_group)
    return res_groups


if __name__ == '__main__':
    # gr_list = enumerate_words(partition(read_file(f), sep_num))
    gr_list = partition(read_file(f), sep_num)
    if not os.path.isdir(target_direct):
        os.mkdir(target_direct)
    for n, i in enumerate(gr_list):
        _file = os.path.join(target_direct, "words_" + str(n) + ".txt")
        save_file(_file, i)

    print("создано {} файлов".format(len(os.listdir(target_direct))))

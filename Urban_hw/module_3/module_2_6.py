# Пространство имен и способы вызова функции
# Задача("Однокоренные")
def single_root_words(root_word, *other_words):
    same_words = []
    i = 0
    while i < len(other_words):  #перебор слов
        rw_l = root_word.lower()
        rw = list(rw_l)
        ow_l = other_words[i].lower()
        ow = list(ow_l)
        pass_ = False  # флаг сходства
        for j in range(len(rw)):
            count_ = 0
            pass_list = []
            for k in range(len(ow)):
                if rw[j] == ow[k]:  # поиск корней
                    pass_ = True
                    pass_list.append(pass_)
                    count_ = pass_list.count(True)
                    if count_ == len(ow):  # условие 1 добавления слова в список
                        same_words.append(other_words[i])
                        break
                    elif count_ == len(rw):  # условие 2 добавления слова в список
                        same_words.append(other_words[i])
                        break
                if pass_ == True:  # при совпадении, переключить ячейки
                    j += 1
                    k += 1
            if pass_ == False:  # в случае несовпадения по началу, переключить ячейку и продолжить
                j += 1
                continue
            break
        i += 1
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement',  'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

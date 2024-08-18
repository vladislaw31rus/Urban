# Пространство имен и способы вызова функции
# old name 'module_2_6.py'
'@''''
Цель: закрепить знание использования параметров *args/ **kwargs на практике.

Задача "Однокоренные":
Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.

Пункты задачи:
1. Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
2. Создайте внутри функции пустой список same_words, который пополнится нужными словами.
3. При помощи цикла for переберите предполагаемо подходящие слова.
4. Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
5. После цикла верните образованный функцией список same_words.
6. Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
Пример результата выполнения программы:
Исходный код:
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
Вывод на консоль:
['richiest', 'orichalcum', 'richies']
['Able', 'Disable']
Примечания:
При проверке наличия одного слова в составе другого стоит учесть, что регистр символов не должен влиять ни на что. ('Disablement' - 'Able') ('Able', 'able', 'AbLe' - все подходят)
В этой задаче вам могут понадобиться следующие методы строк/ключевые слова:
а. Оператор in или count()
b. lower()/upper().
'@'''''

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


# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result2 = single_root_words('Disablement',  'Able', 'Mable', 'Disable', 'Bagel')
# print(result1)
# print(result2)

def srw(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words
result1 = srw('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = srw('Disablement',  'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
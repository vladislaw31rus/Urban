
collection = [1,2,3,4,5,6,7,8,9,10]

def a1(x):
    pass

def a2(x):
    pass

# result = map(a1, filter(a2, collection))
# print(list(result))


#  генерация списков с помощью новой операции. только for. аналог map
list_comp_1 = [x*2 for x in collection]
print(list_comp_1)

# генерация списков с фильтрацией
list_comp_2 = [x*2 for x in collection if x > 5]
print(list_comp_2)

# условия в начале . изменение операции над элементом
list_comp_3 = [x*2 if x > 5 else x*10 for x in collection]
print(list_comp_3)

spisok = ['a', 2, 'b', 4, 'c', 6, 'd', 8, 'e', 10]
sp = [x if type(x) == str else x*10 for x in spisok]
print(sp)

# вложенные списки. генерация двух элементов
collection_2 = [1,2,3,4,5,6,7,8,9,10]
list_comp_4 = [x * y for x in collection for y in collection_2 if x < 3]
print(list_comp_4)

# можно создавать множества и словари
list_comp_5 = {x for x in collection}
print(list_comp_5)
list_comp_6 = {x: x*3 for x in collection}
print(list_comp_6)
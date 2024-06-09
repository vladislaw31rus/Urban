#Словари и множества
my_dict = {'water':10, 'salt':3, 'pepper':1}
print('dict:',my_dict)
print('existing value:',my_dict['water'])
print('not existing value:',my_dict.get('cola'))
my_dict.update({'cola':4, 'potato':25})
del_val = my_dict.pop('potato')
print('deleted value:',del_val)
print('update dict:',my_dict)
my_set = {1, 2, 3, 3, 3, 2,'String' }
print('my_set:',my_set)
my_set.update({20,23,55,18})
my_set.remove('String')
print('new my_set:',my_set)
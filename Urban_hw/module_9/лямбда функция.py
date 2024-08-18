# принимает х и добавляет к нему 10
my_f = lambda x: x + 10

print(my_f(x=33))

collect_ = [1,2,3,4,5,6,7,8,9]
result = map(lambda x: x+10, collect_)
print(list(result))

collect_2 = [19,18,17,16,15,14,13,12,11]
result = map(lambda x,y: x+y, collect_, collect_2)
print(list(result))
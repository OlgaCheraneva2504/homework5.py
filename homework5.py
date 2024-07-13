immutable_var = 1, 'c', 2, 'd', True
print(immutable_var)
# immutable_var[0] = 17, Нельзя изменить элемент кортежа, так как кортеж является неизменяемым объектом

mutable_list = [4, 'c', 25, 'f', True]
print(mutable_list)
mutable_list[2] = 'Den'
print(mutable_list)

immutable_var = tuple_ = (0.5, 1, True ,'Dog')
print(immutable_var)
# immutable_var.append(100)
# immutable_var.extend("cat")
# immutable_var.remove(True)
# immutable_var.upper()
# immutable_var [0] = 15
# Так как кортежи неизменяемые, все команды выше и т. п. будут выдавать ошибку "TypeError: 'tuple' object does not support item assignment"
# Но кортежи поддерживают два вида операций: конкатенацию и умножение. Например:
# Умножение:
#print(immutable_var * 2)
# Конкатенация:
#tuple_1 = (1, 2, 3)
#tuple_2 = (4, 5, 6)
#concatenated_tuple = tuple_1 + tuple_2
#print(concatenated_tuple)
# Кортеж неизменяемый, но может хранить изменяемую информацию, например, списки, которые мы можем изменить
#tuple_ = ([1, 2], 4, 5, 100)
#print(tuple_)
#tuple_[0][0] = 50
#print(tuple_)
mutable_list = [1.5, 2, False,'Cat']
mutable_list.append(100)
mutable_list.extend("bear")
mutable_list.remove(2)
mutable_list [0] = 15
print(mutable_list*2)
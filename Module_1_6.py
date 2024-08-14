my_dict={'Andrei': 1962, 'Tatyna': 1959, 'Vasiliy': 1987, 'Aleksandr': 2003}
print(my_dict)# Выведите на экран словарь my_dict.
print(my_dict['Andrei'])# Выведите на экран одно значение по существующему ключу
my_dict['grigorii']= 2002
print(my_dict) # Выведите на экран словарь my_dict.
print(my_dict['grigorii']) # Выведите на экран одно по отсутствующему из словаря my_dict
my_dict[('Anatolii')]= 1967 # Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict['Irina']= 1964
print(my_dict) # # Выведите на экран словарь my_dict.
a=my_dict.pop('Irina')# Удалите одну из пар в словаре по существующему ключу
print(my_dict)  # Выведите на экран словарь my_dict.
print(a)
#
#
my_set={1,2,3,4,5,1,2,3,'slovo',(3,14)} # Создайте переменную и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями
print(my_set)# Выведите на экран множество (должны отобразиться только уникальные значения)
print(my_set.add('mnogestvo'))
print(my_set.add(10))
print(my_set)
print(my_set.discard('slovo'))
print(my_set)


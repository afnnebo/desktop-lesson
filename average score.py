grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_m=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),
          sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),
          sum(grades[4])/len(grades[4])] # вычисляем средние значения в списках
print(grades_m) # выводим на консоль
#
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students) # сортируем множество по алфавиту.
print(students_sort) # выводим на консоль.
#
dict1 = dict(zip(students_sort,grades_m)) # Полученные данные объединяем и преобразуем в словарь имеющий ключ и значение.
print(dict1)

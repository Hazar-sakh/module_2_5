# Задача "Матрица воплоти"

# Блок ввода данных

n = int(input('Впишите количество строк матрицы: '))
m = int(input('Впишите количество столбцов матрицы: '))
value = int(input('Впишите значение для матрицы: '))


# Задаем функцию
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):  # цикл n-е количество раз \/
        matrix.append([])  # добавляет список в список matrix
        for j in range(m):  # цикл m-е количество раз \/
            matrix[i].append(value)  # вписывает во вложенный список value
    return matrix  # возвращаем переменную matrix после выполнения функции


# выводим результат
result = get_matrix(n, m, value)
print('\nВаша матрица:\n' + str(result))

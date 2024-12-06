import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Ввод функции от пользователя
func_input = input("Введите функцию f(x): ")
x = sp.symbols('x')

# Преобразование строки в функцию
func = sp.sympify(func_input)

# Генерация массива x
x_arr = np.linspace(-5, 5, 200)

# Вычисление значений функции для массива x
y_arr = [func.subs(x, val) for val in x_arr]

# Настройки графика
plt.figure()
plt.plot(x_arr, y_arr, label=f'f(x) = {func_input}')
plt.grid()
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции')
plt.legend(loc='upper left')

# Сохранение графика
plt.savefig('1.png')
plt.show()

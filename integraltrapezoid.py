import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

import numpy as np
import sympy
from sympy import symbols

x = symbols('x')

func = sympy.sympify(input())
a = float(input())
b = float(input())
n = int(input())

x_arr = np.linspace(a - 0.5, b + 0.5, 200)

plt.grid()

mini = float(sympy.minimum(func, x, sympy.Interval(a - 0.5, b + 0.5)) - 0.5)
maxi = float(sympy.maximum(func, x, sympy.Interval(a - 0.5, b + 0.5)) + 0.5)

plt.xlim(a - 0.5, b + 0.5)
plt.ylim(mini, maxi)

plt.plot(x_arr, [0] * 200)
plt.plot(x_arr, [func.subs(x, point) for point in x_arr])
plt.axvline(x=a, linestyle=':', color='red')
plt.axvline(x=b, linestyle=':', color='red')

plt.plot(a, func.subs(x, a), 'o', color='red')

dx = np.linspace(a, b, n)
summ = 0

for i in range(n - 1):
    value_x1 = dx[i]
    value_x2 = dx[i + 1]
    value_y1 = func.subs(x, dx[i])
    value_y2 = func.subs(x, dx[i + 1])
    h = dx[i + 1] - dx[i]
    summ += h * (value_y1 + value_y2) / 2

    xx = [value_x1, value_x1, value_x2, value_x2]
    yy = [0, value_y1, value_y2, 0]
    plt.gca().add_patch(Polygon(xy=list(zip(xx, yy)), edgecolor='green', facecolor='green', alpha=0.5))
    plt.plot(value_x2, value_y2, 'o', color='red')

real_integ = sympy.integrate(func, (x, a, b))

print("Вычисленный интеграл: ", summ)
print("Правильный интеграл: ", real_integ)
print("Модуль разницы: ", np.abs(summ - real_integ))

plt.savefig('1.png')
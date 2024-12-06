import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import numpy as np
import sympy
from sympy import symbols

x = symbols('x')

func = sympy.sympify(input())
a = float(input())
b = float(input())
n = 2

summ = 0
real_integ = sympy.integrate(func, (x, a, b))

while(np.abs(summ - real_integ)>0.001):
    dx = np.linspace(a, b, n)

    summ = 0

    for i in range(n-1):
        value_x = dx[i]
        value_y = func.subs(x,(dx[i]+dx[i+1])/2)
        h = dx[i+1]-dx[i]
        summ += h*value_y
    n+=1

print("Минимальное значение n: ", n-1)
print("Вычисленный интеграл: ", summ)
print("Правильный интеграл: ", real_integ)
print("Модуль разницы: ", np.abs(summ - real_integ))
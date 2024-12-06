import numpy as np
import sympy
from IPython.display import display
from sympy import symbols
import matplotlib.pyplot as plt
from sympy import sqrt, exp, cos, sin, log

def print_latex(expr):
    print("$", sympy.latex(expr), "$")
x = sympy.symbols('x')
x1 = np.linspace(-5, 5, 100)

y = sympy.sympify(input())
y1 = y.subs(x,x1)
plt.grid()
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# x = np.linspace(0,3,10)
# y = sympy.sympify(x**8)



plt.plot(x,y)
plt.savefig('2.png')
# x,a,b = symbols('x a b')
# func = sympy.sympify((a*x**b)/(a+b))
# print("Выражение:")
#
# print("Корни:")
# # print(sympy.solve(func, x))

import sympy
from sympy import symbols
from sympy import sqrt, exp, cos, sin, log


def print_latex(expr):
    print("$", sympy.latex(expr), "$")


from sympy import oo

x, y = symbols('x y')

expr = -x ** 2 + 2 * x + 5
print("Выражение:")
print_latex(expr)
print("Максимум на $(-\infty, \infty)$:")
print(sympy.maximum(expr, x, sympy.Interval(-oo, oo)))
print("Минимум на $[3, 5]$:")
print(float(sympy.minimum(expr, x, sympy.Interval(3, 5))))
print(type(sympy.minimum(expr, x, sympy.Interval(3, 5))))
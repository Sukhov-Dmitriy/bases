import sympy
from sympy import symbols
from sympy import sqrt, exp, cos, sin, log


def print_latex(expr):
    print("$", sympy.latex(expr), "$")


from sympy import oo

x = symbols('x')
expr = sympy.sympify(exp(x)/x)

print("Выражение:")
print_latex(expr)
print("Особая точка:")
p = sympy.singularities(expr, x)
print(p)
print("Предел слева:")
lim = sympy.Limit(expr, x, p.args[0], "-")
print_latex(lim.doit())
print("Предел справа:")
lim = sympy.Limit(expr, x, p.args[0], "+")
print_latex(lim.doit())
print("Предел в плюс бесконечности:")
lim = sympy.Limit(expr, x, oo)
print_latex(lim.doit())
print("Предел в минус бесконечности:")
lim = sympy.Limit(expr, x, -oo)
print_latex(lim.doit())
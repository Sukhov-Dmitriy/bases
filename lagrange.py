import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6, 6))
plt.grid(True)

x = np.linspace(-2, 2, 5)
func = lambda x: np.exp(-x / 3) + x ** 3 + 0.2
y = func(x)


def basis(i, x0, x, y):
    lbas = y[i]
    for j in range(len(x)):
        if i == j:
            continue
        lbas *= (x0 - x[j]) / (x[i] - x[j])
    return lbas


def lagrange(x0, x, y):
    lagr = 0
    for i in range(len(x)):
        lagr += basis(i, x0, x, y)
    return lagr


xnew = np.linspace(-2, 2, 100)

plt.plot(xnew, [lagrange(x0, x, y) for x0 in xnew], label='Интерполяция полиномом Лагранжа')

plt.plot(xnew, func(xnew), linestyle=":", linewidth=5, color='orange', label='Изначальная функция')
plt.plot(x, y, 'o', color='green', label='Известные точки');

plt.legend()
plt.savefig('1.png')
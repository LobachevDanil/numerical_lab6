import matplotlib.pyplot as plt
import math

N = [10, 20]
y0 = 0
yn = math.exp(1) + math.exp(-1) - 2
a, b = 0, 1
eps = 0.5 * 10 ** (-4)


def y_solution(x):
    return math.exp(x) + math.exp(-x) + 3 * x * x - 3 * x - 2


def p(x):
    return 1


def q(x):
    return 8 + 3 * x * (1 - x)


def tridiagonal_method(n):
    h = (b - a) / n
    A = [2 + h * h * p(a + h * i) for i in range(1, n + 1)]
    B = [h * h * q(a + h * i) for i in range(0, n + 1)]
    lam = [0]
    mu = [0]
    for i in range(1, n + 1):
        lam.append(1 / (A[i - 1] - lam[i - 1]))
        mu.append((mu[i - 1] - B[i]) / (A[i - 1] - lam[i - 1]))
    lam[n] = 0
    y = [yn]
    for i in range(n, 0, -1):
        y.append(lam[i - 1] * y[n - i] + mu[i - 1])
    y.reverse()
    return y


for n in N:
    x = [a + i * (b - a) / n for i in range(n + 1)]
    y = tridiagonal_method(n)
    plt.plot(x, y, label=f"N={n}")

x_data = [a + i * (b - a) / 300 for i in range(301)]
y_data = list(map(y_solution, x_data))
plt.plot(x_data, y_data, label="y(x)")
plt.legend()
plt.show()

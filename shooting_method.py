import matplotlib.pyplot as plt
import math

N = [10, 20]
y0 = 0
yn = math.exp(1) + math.exp(-1) - 2
a, b = 0, 1
eps = 0.5 * 10 ** (-4)


def f(x, y):
    return y + 8 + 3 * x * (1 - x)


def y_solution(x):
    return math.exp(x) + math.exp(-x) + 3 * x * x - 3 * x - 2


def euler_method(mu, n):
    y = [y0]
    z = [mu]
    h = (b - a) / n
    x = a
    for i in range(n):
        y_comp = y[i] + h * z[i]
        z.append(z[i] + (h / 2) * (f(x, y[i]) + f(x + h, y_comp)))
        y.append(y[i] + (h / 2) * (z[i] + z[i + 1]))
        x += h
    return y


def shooting_method(n, x0, x1):
    x = x1
    f0 = euler_method(x0, n)[n] - yn

    while True:
        current_y = euler_method(x, n)
        if abs(current_y[n] - yn) < eps:
            break
        x = x - (current_y[n] - yn) * (x - x0) / (current_y[n] - yn - f0)

    print(f"mu={x}")
    return current_y


for n in N:
    x = [a + i * (b - a) / n for i in range(n + 1)]
    y = shooting_method(n, -10, 10)
    plt.plot(x, y, label=f"N={n}")

x_data = [a + i * (b - a) / 300 for i in range(301)]
y_data = list(map(y_solution, x_data))
plt.plot(x_data, y_data, label="y(x)")
plt.legend()
plt.show()

# mu_data = [-100 + i * (200) / 400 for i in range(401)]
# for j in range(20):
#     y_mu_data = list(map(lambda i: euler_method(i, 20)[j], mu_data))
#     plt.plot(mu_data, y_mu_data, label=f"y[{j}](mu)")
#
# plt.legend()
# plt.show()

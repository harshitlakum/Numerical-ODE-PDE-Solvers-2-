import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    A = np.array([[0, 1], [-1, 0]])
    b = np.array([np.sin(t), np.cos(t)])
    return A @ y + b

def rk4_step(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h/2 * k1)
    k3 = f(t + h/2, y + h/2 * k2)
    k4 = f(t + h, y + h * k3)
    return y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

t0 = -2.5
t1 = 10
h = 1/30
N = int((t1 - t0)/h) + 1
t_values = np.linspace(t0, t1, N)
y0 = np.array([2.5 * np.sin(2.5), -2.5 * np.cos(2.5)])

ys = np.zeros((N, 2))
ys[0] = y0

for n in range(N-1):
    ys[n+1] = rk4_step(f, t_values[n], ys[n], h)

plt.figure(figsize=(10, 5))
plt.plot(t_values, ys[:,0], label='$y_1(t)$')
plt.plot(t_values, ys[:,1], label='$y_2(t)$')
plt.xlabel('t')
plt.ylabel('y')
plt.title('RK4 Solution of Linear ODE System')
plt.legend()
plt.grid(True)
plt.show()
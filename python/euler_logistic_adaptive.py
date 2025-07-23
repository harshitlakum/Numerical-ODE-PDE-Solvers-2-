import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return (1 - y / 100) * y

t0, t1 = 0, 10
y0 = 1

tol = 1e-3
h = 0.1
h_min, h_max = 1e-4, 0.5

t_values = [t0]
y_values = [y0]
h_values = []

t = t0
y = y0

while t < t1:
    if t + h > t1:
        h = t1 - t
    y1 = y + h * f(t, y)
    y_half = y + (h/2) * f(t, y)
    y2 = y_half + (h/2) * f(t + h/2, y_half)
    err = abs(y2 - y1)
    if err < tol:
        t += h
        y = y2
        t_values.append(t)
        y_values.append(y)
        h_values.append(h)
        h = min(h_max, h * min(2, 0.9 * (tol / (err + 1e-16))**0.5))
    else:
        h = max(h_min, h * max(0.1, 0.9 * (tol / (err + 1e-16))**0.5))

t_values = np.array(t_values)
y_values = np.array(y_values)
h_values = np.array(h_values)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(t_values, y_values, 'b-', label='Adaptive Euler Solution')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Logistic Growth: Adaptive Euler')
plt.grid()
plt.legend()

plt.subplot(1,2,2)
plt.plot(t_values[1:], h_values, 'r.-')
plt.xlabel('t')
plt.ylabel('Step size h')
plt.title('Step size vs. time')
plt.grid()

plt.tight_layout()
plt.show()
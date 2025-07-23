import numpy as np
import matplotlib.pyplot as plt

s = 1000
A = np.array([[-s, s-1], [0, -1]])
y0 = np.array([2.0, 1.0])

T = 0.01
h = 0.001
N = int(T / h) + 1
t = np.linspace(0, T, N)

def exact_sol(t):
    return np.vstack((np.exp(-s * t) + np.exp(-t), np.exp(-t)))

def implicit_midpoint(A, y0, t, h):
    I = np.eye(A.shape[0])
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    LHS = I - (h/2)*A
    RHS = I + (h/2)*A
    LHS_inv = np.linalg.inv(LHS)
    for k in range(n-1):
        y[k+1] = LHS_inv @ (RHS @ y[k])
    return y

def explicit_euler(A, y0, t, h):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for k in range(n-1):
        y[k+1] = y[k] + h * (A @ y[k])
    return y

y_im = implicit_midpoint(A, y0, t, h)
y_ee = explicit_euler(A, y0, t, h)
y_ex = exact_sol(t).T

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, y_ex[:, 0], 'k-', label='Exact $y_1$')
plt.plot(t, y_im[:, 0], 'b--', label='Implicit Midpoint $y_1$')
plt.plot(t, y_ee[:, 0], 'r:', label='Explicit Euler $y_1$')
plt.title('Component $y_1$')
plt.xlabel('t'); plt.ylabel('y')
plt.legend(); plt.grid()

plt.subplot(1, 2, 2)
plt.plot(t, y_ex[:, 1], 'k-', label='Exact $y_2$')
plt.plot(t, y_im[:, 1], 'b--', label='Implicit Midpoint $y_2$')
plt.plot(t, y_ee[:, 1], 'r:', label='Explicit Euler $y_2$')
plt.title('Component $y_2$')
plt.xlabel('t'); plt.ylabel('y')
plt.legend(); plt.grid()

plt.tight_layout()
plt.show()
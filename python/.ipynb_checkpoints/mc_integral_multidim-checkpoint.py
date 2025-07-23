import numpy as np
import matplotlib.pyplot as plt

def f(x):
    d = x.shape[1]
    js = np.arange(1, d+1)
    return np.prod(np.exp(x) / js, axis=1)

def exact_value(d):
    js = np.arange(1, d+1)
    terms = np.expm1(1/js) / js
    return np.prod(terms)

dims = [1,2,3,4,5,6,7,8,9,10]
N = 100000

mc_estimates = []
stddevs = []
errors = []
exact_vals = []

rng = np.random.default_rng(42)

for d in dims:
    X = rng.uniform(0, 1, size=(N, d))
    vals = f(X)
    mc_mean = np.mean(vals)
    std = np.std(vals) / np.sqrt(N)
    exact = exact_value(d)
    error = abs(mc_mean - exact)
    mc_estimates.append(mc_mean)
    stddevs.append(std)
    errors.append(error)
    exact_vals.append(exact)

print(f"{'d':>2} {'MC Estimate':>13} {'StdDev':>13} {'Exact':>13} {'Error':>13}")
for i, d in enumerate(dims):
    print(f"{d:2d} {mc_estimates[i]:13.8f} {stddevs[i]:13.8f} {exact_vals[i]:13.8f} {errors[i]:13.8f}")

plt.semilogy(dims, errors, 'o-', label='Absolute Error')
plt.semilogy(dims, stddevs, 's-', label='MC StdDev')
plt.xlabel('Dimension d')
plt.ylabel('Error (log scale)')
plt.title('Monte Carlo Integration Error vs Dimension')
plt.legend()
plt.grid(True, which='both')
plt.show()
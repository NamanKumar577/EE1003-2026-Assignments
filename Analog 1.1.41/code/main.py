import numpy as np
import matplotlib.pyplot as plt

# Define unit step
def u(t):
    return np.where(t >= 0, 1.0, 0.0)

# Define unit ramp
def r(t):
    return t * u(t)

# Time axis
t = np.linspace(-1, 6, 10000)
dt = t[1] - t[0]


# Signals to convolve
f1 = u(t + 1)       # u(t+1)
f2 = r(t - 2)       # r(t-2)

# Convolution (numerical)
y_num = np.convolve(f1, f2, mode='full') * dt
t_conv = np.linspace(2*t[0], 2*t[-1], len(y_num))

# Analytical result
y_anal = 0.5 * (t - 1)**2 * u(t - 1)


# Plot
plt.figure(figsize=(8, 4))
plt.plot(t_conv, y_num, 'b-', label='Numerical convolution')
plt.plot(t, y_anal, 'r--', label=r'Analytical: $\frac{1}{2}(t-1)^2 u(t-1)$')
plt.xlim(-1, 6)
plt.ylim(-0.5, 8)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title(r'$u(t+1) * r(t-2)$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("convolution.png", dpi=300)
plt.show()

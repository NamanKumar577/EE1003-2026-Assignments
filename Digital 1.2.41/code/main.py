import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Rewrite ODE: dy/dx from ye^x dx + (4y + e^x) dy = 0
# => dy/dx = -y e^x / (4y + e^x)
def ode(y, x):
    ex = np.exp(x)
    denom = 4*y + ex
    if abs(denom) < 1e-10:
        return 0.0
    return -y * ex / denom

# Solve numerically
x = np.linspace(0, 2, 500)
y0 = [-1.0]
sol = odeint(ode, y0, x)



# Analytical solution: 2y^2 + e^x * y - 1 = 0
# Quadratic formula: y = (-e^x +/- sqrt(e^2x + 8)) / 4
# Use MINUS root to match initial condition y(0) = -1:
# y(0) = (-1 - sqrt(9)) / 4 = (-1-3)/4 = -1  (correct)
def y_analytical(x_vals):
    ex = np.exp(x_vals)
    discriminant = ex**2 + 8
    return (-ex - np.sqrt(discriminant)) / 4

y_anal = y_analytical(x)



plt.figure(figsize=(8, 4))
plt.plot(x, sol, 'b-', label='Numerical (odeint)')
plt.plot(x, y_anal, 'r--', label=r'Analytical: $ye^x+2y^2-1=0$')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Solution of $ye^x\,dx + (4y+e^x)\,dy = 0$, $y(0)=-1$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("image.png", dpi=300)
plt.show()

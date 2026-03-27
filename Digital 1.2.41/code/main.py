import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def ode(y, x):
    ex = np.exp(x)
    denom = 4*y + ex
    if abs(denom) < 1e-10:   
        return 0.0
    return -y * ex / denom
 
x = np.linspace(0, 2, 500)
sol = odeint(ode, [-1.0], x)



def y_analytical(x_vals):
    ex = np.exp(x_vals)
    return (-ex - np.sqrt(ex**2 + 8)) / 4

y_anal = y_analytical(x)


print(f"Analytical y(0) = {y_analytical(np.array([0.0]))[0]:.4f}")



fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

axes[0].plot(x, sol, 'b-', linewidth=2, label='Numerical (odeint)')
axes[0].set_title('Numerical Solution via odeint')
axes[0].set_xlabel('x'); axes[0].set_ylabel('y')
axes[0].legend(); axes[0].grid(True)

axes[1].plot(x, y_anal, 'r--', linewidth=2,
             label=r'Analytical: $ye^x+2y^2-1=0$')
axes[1].set_title(r'Analytical: $y=(-e^x-\sqrt{e^{2x}+8})/4$')
axes[1].set_xlabel('x'); axes[1].set_ylabel('y')
axes[1].legend(); axes[1].grid(True)

plt.suptitle(r'Solution of $ye^x\,dx+(4y+e^x)\,dy=0$, $y(0)=-1$')
plt.tight_layout()
plt.savefig("image.png", dpi=300)
plt.show()

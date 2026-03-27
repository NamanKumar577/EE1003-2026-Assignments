import numpy as np
import matplotlib.pyplot as plt

def u(t):
    return np.where(t >= 0, 1.0, 0.0)

t = np.linspace(-2, 8, 10000)

y_base = 0.5 * t**2 * u(t)

a, b = -1, 2
y_general = 0.5 * (t - a - b)**2 * u(t - a - b)

y_question = 0.5 * (t - 1)**2 * u(t - 1)

fig, axes = plt.subplots(2, 1, figsize=(9, 9), sharex=True)

axes[0].plot(t, y_base, 'b-', linewidth=2)
axes[0].set_title(r'$u(t)*r(t)=\frac{1}{2}t^2 u(t)$  [Base: $a=0,b=0$, onset $t=0$]')
axes[0].set_ylabel('y(t)'); axes[0].grid(True); axes[0].set_ylim(-0.5,9)

axes[1].plot(t, y_question, 'r-', linewidth=2)
axes[1].set_title(r'$u(t+1)*r(t-2)=\frac{1}{2}(t-1)^2 u(t-1)$  [Question, onset $t=1$]')
axes[1].set_ylabel('y(t)'); axes[1].set_xlabel('t')
axes[1].grid(True); axes[1].set_ylim(-0.5,9)

plt.xlim(-2, 8)
plt.tight_layout()
plt.savefig("image.png", dpi=300)
plt.show()

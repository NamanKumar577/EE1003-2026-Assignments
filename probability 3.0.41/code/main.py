import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Given probabilities
P_car   = 0.45
P_pub   = 1 - P_car          # 0.55

P_bus_given_pub   = 0.55
P_metro_given_pub = 1 - P_bus_given_pub   # 0.45

# Joint probabilities
P_bus   = P_pub * P_bus_given_pub    # 0.3025 -> 0.30
P_metro = P_pub * P_metro_given_pub  # 0.2475 -> 0.25

print(f"P(car)   = {P_car:.2f}")
print(f"P(bus)   = {P_bus:.4f} ~ {round(P_bus,2):.2f}")
print(f"P(metro) = {P_metro:.4f} ~ {round(P_metro,2):.2f}")
print(f"Sum      = {P_car+P_bus+P_metro:.4f}")

# Bar chart of probabilities
labels = ['Car', 'Bus', 'Metro']
probs  = [P_car, round(P_bus, 2), round(P_metro, 2)]
colors = ['steelblue', 'darkorange', 'green']

plt.figure(figsize=(7, 4))
bars = plt.bar(labels, probs, color=colors, edgecolor='black', width=0.4)

for bar, val in zip(bars, probs):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.01,
             f'{val:.2f}', ha='center', fontsize=12, fontweight='bold')

plt.ylim(0, 0.6)
plt.ylabel('Probability')
plt.title('Probability of Car, Bus and Metro (CE 2008)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("image.png", dpi=300)
plt.show()

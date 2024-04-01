import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)


plt.plot(x, y, marker='o', linestyle='-', color='b', label='Sine Wave')


plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)
plt.show()
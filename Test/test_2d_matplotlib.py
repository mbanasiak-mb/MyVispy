import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2 + 0.01, 0.25 - 0.01, 1000)
y = 0

px = np.array([])
py = np.array([])

acc = 25
for n in range(0, acc):
    y = y ** 2 + x
    px = np.append(px, x)
    py = np.append(py, y)

plt.plot(px, py, '.b', ms=0.1)

plt.grid(True)
plt.show()

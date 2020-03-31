import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, x, z)
plt.xlabel('x from 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.title("Sine and cosine plot")
plt.legend(['sin(x)', 'cos(x)'])
plt.show()

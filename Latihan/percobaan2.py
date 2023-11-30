import matplotlib.pyplot as plt
import numpy as np

xPoints = np.array([1, 8, 10])
yPoints = np.array([3, 10, 5])

plt.figure(figsize = (5, 5))
plt.plot(xPoints, yPoints, color = 'red')
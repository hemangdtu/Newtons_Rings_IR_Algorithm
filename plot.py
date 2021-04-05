import matplotlib.pyplot as plt
import numpy as np
import sys

distances = np.array([float(i) for i in open("converted.txt", 'r').read().split('\n')[:-1]])

print(distances)

cf, cov = np.polyfit([i + 1 for i in range(0, len(distances))], distances ** 2, 1, cov=True)
line = np.poly1d(cf)

print("Slope: ", cf[0])
print("Variance in Slope: ", cov[0][0])
# calculate curvature
wavelength = 589.3e-6
curv = cf[0] / (4.0 * wavelength)

print("Curvature (mm): ", curv)


plt.ylabel(r"Distance squared (mm$^{2}$)")
plt.xlabel("Number of line")
plt.plot([i + 1 for i in range(0, len(distances))], distances ** 2, 'ko')
plt.plot([0,13], [line(0), line(13)])
plt.show()

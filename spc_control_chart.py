import numpy as np

np.random.seed(42)
data = np.random.normal(loc=50, scale=2, size=100)

# Inject anomalies
data[20] = 60
data[75] = 40

mean = np.mean(data)
std = np.std(data)

UCL = mean + 3 * std
LCL = mean - 3 * std

anomalies = [x for x in data if x > UCL or x < LCL]

import matplotlib.pyplot as plt

plt.plot(data, marker='o')
plt.axhline(mean, linestyle='--')
plt.axhline(UCL, linestyle='--')
plt.axhline(LCL, linestyle='--')

plt.title("SPC Control Chart")
plt.show()

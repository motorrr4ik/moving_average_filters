import numpy as np
import matplotlib.pyplot as plt

def moving_average(data, smooth_interval=2):
    sum = 0
    new_data = np.zeros(len(data))
    for i in range(len(data)-smooth_interval):
        for j in range(smooth_interval):
            sum += data[i+j]
        average = sum/smooth_interval
        new_data[i+smooth_interval] = average
        sum = 0
    return new_data

# data = np.array([5.3, 6.7, 7.9, 7.1, 5.2, 4.1, 3.5, 5.4, 7.3, 9.4, 8, 6.6, 7.9, 9.2, 7.6])
# x = [0 for i in range(len(data))]
# n = 3

# new_data = moving_average(data, n)

# plt.plot(data)
# plt.plot(new_data)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

def weighted_moving_average(data, smooth_interval=2):
    sum = 0
    j_sum = 0
    new_data = np.zeros(len(data))
    for i in range(len(data)-smooth_interval):
        for j in range(smooth_interval):
            sum += data[i+j]*(j+1)
            j_sum += (j+1)
        average = (sum)/(j_sum)
        # print("average: ", average)
        new_data[i+smooth_interval] = average
        sum = 0
        j_sum = 0
    return new_data

# t = np.arange(0.0,2.0, 1e-3)
# y = np.sin(t) + np.random.rand(t.shape[0])

# data = np.array([5.3, 6.7, 7.9, 7.1, 5.2, 4.1, 3.5, 5.4, 7.3, 9.4, 8, 6.6, 7.9, 9.2, 7.6])
# n = 5

# new_data = moving_average(y, n)
# print(data)
# print(new_data)

# plt.plot(y)
# plt.plot(new_data)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

def exponential_moving_avereage(data, smooth_interval = 2):

    if smooth_interval >= len(data):
        print("Smooth interval more or equal array lenght!")
        return
    
    alpha = 2.0/(smooth_interval+1)
    filtered_values = np.zeros(len(data))
    sum = 0

    for step in range(smooth_interval):
        sum += data[step]
    previous_ma_value = sum/smooth_interval

    for step in range(smooth_interval, len(data)):
        filtered_values[step] = previous_ma_value
        previous_ma_value = alpha*data[step]+(1-alpha)*previous_ma_value
        # print("Data: ", data[step], "Prev value: ", previous_ma_value)

    return filtered_values
    

# data = np.array([5.3, 6.7, 7.9, 7.1, 5.2, 4.1, 3.5, 5.4, 7.3, 9.4, 8, 6.6, 7.9, 9.2, 7.6])
# n = 4

# new_data = exponential_moving_avereage(data, n)

# plt.plot(data)
# plt.plot(new_data)
# plt.show()


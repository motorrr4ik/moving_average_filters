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

    for step in range(smooth_interval-1):
        previous_ma_value = alpha*data[step]+(1-alpha)*previous_ma_value
        filtered_values[step] = previous_ma_value

    sum = 0

    for step in range(smooth_interval):
        sum += data[step]
    previous_ma_value = sum/smooth_interval
    filtered_values[smooth_interval-1] = previous_ma_value

    for step in range(smooth_interval, len(data)):
        previous_ma_value = alpha*data[step]+(1-alpha)*previous_ma_value
        filtered_values[step] = previous_ma_value

    return filtered_values
    




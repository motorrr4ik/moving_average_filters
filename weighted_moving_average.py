import numpy as np
import matplotlib.pyplot as plt

def weighted_moving_average(data, smooth_interval=2):

    if(smooth_interval > len(data)):
        print("Smooth interval > lenght of data")
        return

    sum = 0
    j_sum = 0
    new_data = np.zeros(len(data))

    for i in range(smooth_interval):
        for j in range(smooth_interval):
            sum += data[i+j]*(j+1)
            j_sum += (j+1)
        average = (sum)/(j_sum)
        new_data[i] = average
        sum = 0
        j_sum = 0

    for i in range(len(data)-smooth_interval):
        for j in range(smooth_interval):
            sum += data[i+j]*(j+1)
            j_sum += (j+1)
        average = (sum)/(j_sum)
        new_data[i+smooth_interval] = average
        sum = 0
        j_sum = 0

    return new_data



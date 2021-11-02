# Moving Average filters realization in python
### Requirements
* `Numpy`
* `Matplotlib`
### Usage 
* clone this repo into your project using `git clone https://github.com/motorrr4ik/moving_average_filters` 
* import method you need. For example `from moving_average import moving_average`
* by default every functions needs 2 arguments: 1) data; 2) smooth_interval. The second one equals 2 by default
### Example 
```python
import numpy as np
import matplotlib.pyplot as plt
from moving_average import exponential_moving_avereage, moving_average, weighted_moving_average

t = np.arange(0.0,2.0, 1e-2)
y = np.sin(t) + np.random.rand(t.shape[0])
n = 25

new_data_exp = exponential_moving_avereage(y, n)
new_data_weight = weighted_moving_average(y, n)
new_data = moving_average(y,n)

plt.plot(y, label = 'Origial')
plt.plot(new_data_exp, label = 'Exp Filtered data')
plt.plot(new_data_weight, label = 'Weight Filtered data')
plt.plot(new_data, label = 'Filtered data')
plt.legend()
plt.show()
```
#### Result
![Result image](https://ibb.co/k9xFY2V)
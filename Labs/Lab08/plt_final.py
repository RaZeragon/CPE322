import matplotlib.pyplot as plt
from pandas import *
from scipy import stats

data = read_csv('rpidata.csv')
x = data['CPU Usage %']
y = data['Temperature C']

# Time series
plt.plot(y, 'r', lw=2, label='Temperature C')
plt.plot(x, 'b', lw=2, label='CPU Usage %')
plt.xticks([80,168,256,343,431],['22:45','23:00','23:15','23:30','23:45'])
plt.xlabel('Time')
plt.legend(loc='lower center')
plt.title('RaZeragonPI Time Series: 2022-05-11')

# Histogram of CPU usage
plt.figure()
num_bins = 35
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue', alpha=0.5)
plt.xlabel('CPU Usage %')
plt.ylabel('Probability')
plt.title('RaZeragonPI CPU Usage Histogram: 2022-05-11')

# Histogram of temperature
plt.figure()
num_bins = 30
n, bins, patches = plt.hist(y, num_bins, density=1, facecolor='red', alpha=0.5)
plt.xlabel('Temperature C')
plt.ylabel('Probability')
plt.title('RaZeragonPI Temperature Histogram: 2022-05-11')

# Horizontal box plot of CPU usage
plt.figure()
plt.boxplot(x, 0, '+', 0)
plt.xlabel('CPU Usage %')
plt.title('RaZeragonPI CPU Usage Box Plot: 2022-05-11')

# Vertical box plot of temperature
plt.figure()
plt.boxplot(y, 0, '+')
plt.ylabel('Temperature C')
plt.title('RaZeragonPI Temperature Box Plot: 2022-05-11')

# Scatter diagram with a linear regression line
plt.figure()
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.xlabel('CPU Usage %')
plt.ylabel('Temperature C')
plt.plot(x, y, 'bo')
l = [slope * i + intercept for i in x]
plt.plot(x, l, 'r', lw=2)
plt.title('RaZeragonPI Scatter Diagram & Linear Regression Line: 2022-05-11')

plt.show()

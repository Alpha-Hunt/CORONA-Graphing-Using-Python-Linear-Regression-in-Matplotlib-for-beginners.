import numpy as np
import pandas as pd
from numpy import polyfit
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

print('done')

#get corona
corona = pd.read_csv('CoronaVirus.csv')

date=corona['Order']
new_cases=corona['New cases']


x=np.array(date)
y= np.array(new_cases)
plt.figure(figsize=(15,10))
plt.plot(x,y,'r--')

m,b=np.polyfit(x,y,1)#m = slope, b = intercept
plt.plot((x),(m*x+b))#add line of best fit

plt.ylabel('New Cases Per Day')
plt.xlabel('Days')

plt.grid(True)
plt.title('Corona in INDIA',fontsize=16)

plt.text(1, 1900, r'Red Line Shows The Rate Of Increasing Number Of Cases')
#print(corona)
plt.show()

# figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
print(round(m*36+b))
print(round(m),round(b))



pip install numpy
	#For More Info :https://numpy.org/doc/
pip install pandas
	#For More Info :https://pandas.pydata.org/docs/
pip install matplotlib
	#For More Info :https://matplotlib.org/3.2.1/contents.html
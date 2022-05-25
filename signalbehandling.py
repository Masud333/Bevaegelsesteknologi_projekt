# -*- coding: utf-8 -*-
"""
Created on Mon May 23 07:30:31 2022

@author: masud
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from scipy.signal import find_peaks
from detecta import detect_peaks
from scipy import signal

angle = 90
angle_procent = 0.1

######### LOAD DATA 1
x = np.loadtxt('Forsøg_1.txt', delimiter = ',', dtype=str)
x[0] = re.sub(r'ï»¿', '', x[0])
reshaped = x.reshape(-1,len(x)).T
df_1 = pd.DataFrame(data = reshaped[0:,:], columns = reshaped[0])
df_1.columns =['Knee angle_1']
df_1['Knee angle_1'] = pd.to_numeric(df_1['Knee angle_1'])




######### LOAD REST OF THE DATA 2 - 6
x = np.loadtxt('Forsøg_2.txt', delimiter = ',', dtype=str)
x[0] = re.sub(r'ï»¿', '', x[0])
reshaped = x.reshape(-1,len(x)).T
df_2 = pd.DataFrame(data = reshaped[0:,:], columns = reshaped[0])
df_2.columns =['Knee angle_2']
df_2['Knee angle_2'] = pd.to_numeric(df_2['Knee angle_2'])
######### LOAD DATA 3
x = np.loadtxt('Forsøg_3.txt', delimiter = ',', dtype=str)
x[0] = re.sub(r'ï»¿', '', x[0])
reshaped = x.reshape(-1,len(x)).T
df_3 = pd.DataFrame(data = reshaped[0:,:], columns = reshaped[0])
df_3.columns =['Knee angle_3']
df_3['Knee angle_3'] = pd.to_numeric(df_3['Knee angle_3'])
######### LOAD DATA 4
x = np.loadtxt('Forsøg_4.txt', delimiter = ',', dtype=str)
x[0] = re.sub(r'ï»¿', '', x[0])
reshaped = x.reshape(-1,len(x)).T
df_4 = pd.DataFrame(data = reshaped[0:,:], columns = reshaped[0])
df_4.columns =['Knee angle_4']
df_4['Knee angle_4'] = pd.to_numeric(df_4['Knee angle_4'])
######### LOAD DATA 5
x = np.loadtxt('Forsøg_5.txt', delimiter = ',', dtype=str)
x[0] = re.sub(r'ï»¿', '', x[0])
reshaped = x.reshape(-1,len(x)).T
df_5 = pd.DataFrame(data = reshaped[0:,:], columns = reshaped[0])
df_5.columns =['Knee angle_5']
df_5['Knee angle_5'] = pd.to_numeric(df_5['Knee angle_5'])
######### LOAD DATA 6
x = np.loadtxt('Forsøg_6.txt', delimiter = ',', dtype=str)
x[0] = re.sub(r'ï»¿', '', x[0])
reshaped = x.reshape(-1,len(x)).T
df_6 = pd.DataFrame(data = reshaped[0:,:], columns = reshaped[0])
df_6.columns =['Knee angle_6']
df_6['Knee angle_6'] = pd.to_numeric(df_6['Knee angle_6'])




###################################### FIND PEAKS METHOD 1
# ######## FIND PEAKS DATA 1
peaks_index_1, _ = find_peaks(df_1['Knee angle_1'], height=(angle - (angle*angle_procent)), distance=52)
peaks_1 = list(df_1['Knee angle_1'][i] for i in peaks_index_1)
peak_diferences_1 = [x - angle for x in peaks_1]
average_peak_1 = sum(peak_diferences_1) / len(peak_diferences_1)
freq_of_peaks_1 = np.diff(peaks_index_1)
average_freq_peaks_1 = sum(freq_of_peaks_1) / len(freq_of_peaks_1)
# ######## FIND PEAKS DATA 2
peaks_index_2, _ = find_peaks(df_2['Knee angle_2'], height=(angle - (angle*angle_procent)), distance=52)
# peaks_2 = list(df_2['Knee angle_2'][i] for i in peaks_index_2)
# peak_diferences_2 = [x - angle for x in peaks_2]
# average_peak_2 = sum(peak_diferences_2) / len(peak_diferences_2)
# freq_of_peaks_2 = np.diff(peaks_index_2)
# average_freq_peaks_2 = sum(freq_of_peaks_2) / len(freq_of_peaks_2)
# ######## FIND PEAKS DATA 3
peaks_index_3, _ = find_peaks(df_3['Knee angle_3'], height=(angle - (angle*angle_procent)), distance=52)
# peaks_3 = list(df_3['Knee angle_3'][i] for i in peaks_index_3)
# peak_diferences_3 = [x - angle for x in peaks_3]
# average_peak_3 = sum(peak_diferences_3) / len(peak_diferences_3)
# freq_of_peaks_3 = np.diff(peaks_index_3)
# average_freq_peaks_3 = sum(freq_of_peaks_3) / len(freq_of_peaks_3)
# ######## FIND PEAKS DATA 4
peaks_index_4, _ = find_peaks(df_4['Knee angle_4'], height=(angle - (angle*angle_procent)), distance=52)
peaks_4 = list(df_4['Knee angle_4'][i] for i in peaks_index_4)
peak_diferences_4 = [x - angle for x in peaks_4]
average_peak_4 = sum(peak_diferences_4) / len(peak_diferences_4)
freq_of_peaks_4 = np.diff(peaks_index_4)
average_freq_peaks_4 = sum(freq_of_peaks_4) / len(freq_of_peaks_4)
# ######## FIND PEAKS DATA 5
peaks_index_5, _ = find_peaks(df_5['Knee angle_5'], height=(angle - (angle*angle_procent)), distance=52)
# peaks_5 = list(df_5['Knee angle_5'][i] for i in peaks_index_5)
# peak_diferences_5 = [x - angle for x in peaks_5]
# average_peak_5 = sum(peak_diferences_5) / len(peak_diferences_5)
# freq_of_peaks_5 = np.diff(peaks_index_5)
# average_freq_peaks_5 = sum(freq_of_peaks_5) / len(freq_of_peaks_5)
# ######## FIND PEAKS DATA 6
peaks_index_6, _ = find_peaks(df_6['Knee angle_6'], height=(angle - (angle*angle_procent)), distance=52)
peaks_6 = list(df_6['Knee angle_6'][i] for i in peaks_index_6)
peak_diferences_6 = [x - angle for x in peaks_6]
average_peak_6 = sum(peak_diferences_6) / len(peak_diferences_6)
freq_of_peaks_6 = np.diff(peaks_index_6)
average_freq_peaks_6 = sum(freq_of_peaks_6) / len(freq_of_peaks_6)




###################################### FIND PEAKS METHOD 2
######## DATA 1
widths_1 = np.arange(1,40) # Widths range should cover the expected width of peaks of interest.
peak_idx_1 = signal.find_peaks_cwt(df_1['Knee angle_1'], widths_1)
# Find valleys(min)
inv_data_y_1 = df_1['Knee angle_1']*(-1) # Tried 1/data_y but not better.
valley_idx_1 = signal.find_peaks_cwt(inv_data_y_1, widths_1)
valley_idx_1 = np.append(valley_idx_1, 249)

######## DATA 3
widths_4 = np.arange(1,60) # Widths range should cover the expected width of peaks of interest.
peak_idx_4 = signal.find_peaks_cwt(df_4['Knee angle_4'], widths_4)
# Find valleys(min)
inv_data_y_4 = df_4['Knee angle_4']*(-1) # Tried 1/data_y but not better.
valley_idx_4 = signal.find_peaks_cwt(inv_data_y_4, widths_4)


######## DATA 6
widths_6 = np.arange(1,40) # Widths range should cover the expected width of peaks of interest.
peak_idx_6 = signal.find_peaks_cwt(df_6['Knee angle_6'], widths_6)
peak_idx_6 = peak_idx_6[1:]
# Find valleys(min)
inv_data_y_6 = df_6['Knee angle_6']*(-1) # Tried 1/data_y but not better.
valley_idx_6 = signal.find_peaks_cwt(inv_data_y_6, widths_6)
valley_idx_6 = np.append(valley_idx_6, 341)


####### ALLIGNING BY FIRST PEAK
df_1['Knee angle_1_sliced'] = df_1.iloc[(peaks_index_1[0]-50):,0]
df_2['Knee angle_2_sliced'] = df_2.iloc[(peaks_index_2[0]-50):,0]
df_3['Knee angle_3_sliced'] = df_3.iloc[(peaks_index_3[0]-50):,0]
df_4['Knee angle_4_sliced'] = df_4.iloc[(peaks_index_4[0]-50):,0]
df_5['Knee angle_5_sliced'] = df_5.iloc[(peaks_index_5[0]-50):,0]
df_6['Knee angle_6_sliced'] = df_6.iloc[(peaks_index_6[0]-50):,0]







########## PRE-PROCESSING FOR BEST FIT LINE (RED)
# x = [55, 100, 138, 175, 207, 249]
# y = [-3.23275, 3.43207, 6.52023, 11.5892, 16.3193, 12.2996]
# dt = np.array([[55,-3.23275], [100, 3.43207], [138, 6.52023], [175, 11.5892], [207, 16.3193], [249, 12.2996]]) ### FORSØG 1
dt = np.array([[52,3.82505], [112, 7.21099], [172, 4.39906], [226, 7.15764], [279, 7.77249], [341, 8.80037]]) ### FORSØG 6
# Preparing X and y data from the given data
x = dt[:, 0].reshape(dt.shape[0], 1)
X = np.append(x, np.ones((dt.shape[0], 1)), axis=1)
y = dt[:, 1].reshape(dt.shape[0], 1)
# Calculating the parameters using the least square method
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
# Now, calculating the y-axis values against x-values according to the parameters theta0 and theta1
y_line = X.dot(theta)


######### PLOTS
ax = plt.gca() ###gca --> get current axis


# df_1.plot(kind='line',y='Knee angle_1', ax=ax)
# df_2.plot(kind='line',y='Knee angle_2', ax=ax)
# df_3.plot(kind='line',y='Knee angle_3', ax=ax)
df_4.plot(kind='line',y='Knee angle_4', ax=ax)
# df_5.plot(kind='line',y='Knee angle_5_sliced', ax=ax)
# df_6.plot(kind='line',y='Knee angle_6', ax=ax)

# Plot peaks
peak_x = peak_idx_4
peak_y = df_4['Knee angle_4'][peak_idx_4]
ax.plot(peak_x, peak_y, marker='o', linestyle='dashed', color='green', label="Peaks")
# Plot valleys
valley_x = valley_idx_4
valley_y = df_4['Knee angle_4'][valley_idx_4]
ax.plot(valley_x, valley_y, marker='o', linestyle='dashed', color='red', label="Valleys")

# plt.plot(x, y_line, 'r')
plt.title('Find peaks and valleys using find_peaks_cwt()')
plt.legend(loc='best')
# plt.legend(loc='lower right')
# plt.show()

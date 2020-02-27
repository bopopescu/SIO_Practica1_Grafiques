# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#PEL TEMA DE LA DESVIACIÓ CAL MOSTRAR EL PUNT DE LA MITJANA I LLAVORS SI ESTA DESVIAT O NO.

file1 = open('../Resultats/histograma.txt', 'r')
Lines = file1.readlines()

xlabel=[]
frequenciesS=[]
bins=0
max=-99
min=1000000
for line in Lines:
    if line.strip().split(";")[0] !='interval':
        xlabel+=[line.strip().split(";")[0]]
        bins=bins+1
        frequenciesS+=[line.strip().split(";")[1]]
        if max < int(line.strip().split(";")[1]):
            max=int(line.strip().split(";")[1])
        if min > int(line.strip().split(";")[1]):
            min = int(line.strip().split(";")[1])

freq=[]
rang=(min, max)
for freqS in frequenciesS:
    freq+=[int(freqS)]
freq_series = pd.Series(np.array(freq))
#plt.figure(figsize=(12,8))
ax = freq_series.plot(kind='bar')
ax.set_title('Histograma')
ax.set_xlabel('Dades')
ax.set_ylabel('Freqüència')
ax.set_xticklabels(xlabel)
plt.savefig('../Grafics/histograma.png', bbox_inches='tight')
plt.show()


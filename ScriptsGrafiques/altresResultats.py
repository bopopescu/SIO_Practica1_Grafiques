import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

freq=[1688908 , 12482,  2394970 ]
xlabel=['Vots Negatius', 'Vots zero', 'Vots positius']
freq_series = pd.Series(np.array(freq))
#plt.figure(figsize=(12,8))
ax = freq_series.plot(kind='bar')
ax.set_title('Relació entre vots')
ax.set_xlabel('Dades')
ax.set_ylabel('Nombre caselles')
ax.set_xticklabels(xlabel)
plt.savefig('../Grafics/VotsPositusVSVotsNegatiusVsVotszero.png', bbox_inches='tight')
plt.show()

activities = ['Aprobats', 'Suspesos']
slices=[70,30]
colors=['g', 'r']
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0.1,0), radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.title('Percentatge de restaurants Aprobats/Suspesos')
plt.savefig('../Grafics/restaurantsAprobatsSuspesos.png', bbox_inches='tight')
plt.show()

f1 = open('../Resultats/mitjanaUsuaris.txt','r')
lines = f1.readlines()

mitjanesUsuaris=[]
for line in lines:
    if line.split(',')[0] != 'idUsuari':
        mitjanesUsuaris.append(float(line.split(',')[1]))

i=0
for mitjana in mitjanesUsuaris:
    if mitjana > 0:
        i=i+1
percentPositius = (i/len(mitjanesUsuaris)) * 100

i=0
for mitjana in mitjanesUsuaris:
    if mitjana < 0:
        i=i+1
percentNegatius = (i/len(mitjanesUsuaris)) * 100

print('positius: '+str(percentPositius))
print('negatius: '+str(percentNegatius))

activities = ['Positius', 'Negatius']
slices=[percentPositius,percentNegatius]
colors=['g', 'r']
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0.1,0), radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.title('Percentatge d\'usuaris Positius/Negatius')
plt.savefig('../Grafics/usuarisPositiusNegatius.png', bbox_inches='tight')
plt.show()


freq=[3245740,4096360]
xlabel=['Buides', 'Plenes']
freq_series = pd.Series(np.array(freq))
#plt.figure(figsize=(12,8))
ax = freq_series.plot(kind='bar')
ax.set_title('Caselles buides/plenes')
ax.set_xlabel('Dades')
ax.set_ylabel('Nombre caselles')
ax.set_xticklabels(xlabel)
plt.savefig('../Grafics/puntuacionsBuidesvsPlenes.png', bbox_inches='tight')
plt.show()


file1 = open('../Resultats/influenciaGent.txt', 'r')
Lines = file1.readlines()

left=[]
height=[]
for line in Lines:
    if line.split(",")[0] != 'idRestaurant':
        left+=[int(line.split(",")[0])]
        height+=[int(line.split(",")[1])]


# plotting a bar chart
plt.bar(left, height)

# naming the x-axis
plt.xlabel('Restaurant')
# naming the y-axis
plt.ylabel('Vegades visitat')
# plot title
plt.title('Influència de persones')
plt.savefig('../Grafics/influenciaGent.png', bbox_inches='tight')
# function to show the plot
plt.show()
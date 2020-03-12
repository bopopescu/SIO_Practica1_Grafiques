import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as mariadb

file1=open('../Resultats/mitjanaUsuaris.txt', 'r')
Lines=file1.readlines()

mitjana=[]

for line in Lines:
    if line.split(',')[0]!='idUsuari':
        mitjana.append(float(line.split(',')[1]))
mitjanesPerGrups=[]

i=0
sum=0
m=0.0
for mitja in mitjana:
    sum+=mitja
    if i == 10000:
        m=sum/10000.0
        mitjanesPerGrups.append(m)
        i=0
        sum=0
    i=i+1
numElems=[]
i=1
while i<=len(mitjanesPerGrups):
    numElems.append(i)
    i=i+1

file1 = open('../Resultats/desviacioESTPOBXUsuari.txt')
Lines = file1.readlines()
desvestp = []

for line in Lines:
    desvestp.append(float(line.split(',')[1]))

i=0
sum=0
m=0.0
desvestGrup=[]
for desviacio in desvestp:
    sum+=desviacio
    if i == 10000:
        m=sum/10000.0
        desvestGrup.append(m)
        i=0
        sum=0
    i=i+1

print(len(desvestp))


# Create a figure with customized size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Set the axis lables
ax.set_xlabel('Mitjanes', fontsize = 18)
ax.set_ylabel('Desviació', fontsize = 18)
ax.set_title('Mitjanes/Desviacio')
# X axis is day numbers from 1 to 15
xaxis = numElems

# Line color for error bar
color_City_A = 'red'
# Line style for each dataset
lineStyle_City_A={"linestyle":"--", "linewidth":2, "markeredgewidth":2, "elinewidth":2, "capsize":3}
# Create an error bar for each dataset
line_City_A=ax.errorbar(xaxis, mitjanesPerGrups, yerr=desvestGrup, **lineStyle_City_A, color=color_City_A, label='City A')
plt.savefig('../Grafics/putalocura1.png', bbox_inches='tight')
plt.show()
"""
file1 = open('../Resultats/totesPuntuacions.txt', 'r')
Lines = file1.readlines()

puntuacions=[]
for line in Lines:
    puntuacions.append(float(line))

mitjana = np.mean(puntuacions)

print(mitjana)

desvestp = np.std(puntuacions)

print(desvestp)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.set_xlabel('Puntuacions', fontsize=18)
ax.set_ylabel('Desviació', fontsize=18)
xaxis=np.array(range(1, 10))
# Line color for error bar
color_City_A = 'red'
# Line style for each dataset
lineStyle_City_A={"linestyle":"--", "linewidth":2, "markeredgewidth":2, "elinewidth":2, "capsize":3}
# Create an error bar for each dataset
line_City_A=ax.errorbar(xaxis, puntuacions, yerr=desvestp, **lineStyle_City_A, color=color_City_A, label='City A')
# Customize the legend font and handle

# Draw a grid for the graph and set face color to the graph
ax.grid(color='lightgrey', linestyle='-')
ax.set_facecolor('w')
"""

"""
file1 = open('../Resultats/influenciaGent.txt', 'r')
Lines = file1.readlines()

influencia=[]
numRestaurant=[]
for line in Lines:
    if line.split(',')[0] != 'idRestaurant':
        influencia.append(int(line.split(',')[1]))
        numRestaurant.append(int(line.split(',')[0]))

file1=open('../Resultats/mitjanaRestaurants.txt', 'r')
Lines = file1.readlines()

mitjanes=[]
for line in Lines:
    if line.split(',')[0] != 'idRestaurant':
        mitjanes.append(float(line.split(',')[1]))

plt.bar(numRestaurant, influencia)
plt.plot(numRestaurant, mitjanes, color='red')
plt.show()
"""

"""
file1 = open('../Resultats/desviacioEstandardPoblacionalPerUsuari.txt', 'r')
Lines = file1.readlines()

desvesp=[]
for line in Lines:
    if line.split(',')[0]!='idUsuari':
        desvesp.append(float(line.split(',')[1]))

file1=open('../Resultats/mitjanaUsuaris.txt', 'r')
Lines=file1.readlines()

mitjana=[]

for line in Lines:
    if line.split(',')[0]!='idUsuari':
        mitjana.append(float(line.split(',')[1]))
mitjanesPerGrups=[]

i=0
sum=0
m=0.0
for mitja in mitjana:
    sum+=mitja
    if i == 10000:
        m=sum/10000.0
        mitjanesPerGrups.append(m)
        i=0
        sum=0
    i=i+1
numElems=[]
i=1
while i<=len(mitjanesPerGrups):
    numElems.append(i)
    i=i+1

plt.plot(numElems, desvesp, color='red')
plt.bar(numElems, mitjanesPerGrups)
plt.show()
"""
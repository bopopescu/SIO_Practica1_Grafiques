import matplotlib.pyplot as plt
import numpy as np

file1 = open('../Resultats/mitjanaUsuaris.txt', 'r')
Lines = file1.readlines()

x=[]
y=[]
for line in Lines:
    if line.split(",")[0] != 'idUsuari':
        x+=[int(line.split(",")[0])]
        y+=[float(line.split(",")[1])]

plt.scatter(x,y, label="mitjanes", color="blue", marker="*", s=30)
plt.xlabel('Usuaris')
plt.ylabel('Mitjanes')
plt.title('Diagrama de dispersió Usuaris')
plt.legend()
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.savefig('../Grafics/diagramaDispersioMitjanaUsuaris.png', bbox_inches='tight')
plt.show()

file1 = open('../Resultats/mitjanaRestaurants.txt', 'r')
Lines = file1.readlines()

x=[]
y=[]
for line in Lines:
    if line.split(",")[0] != 'idRestaurant':
        x+=[int(line.split(",")[0])]
        y+=[float(line.split(",")[1])]

plt.scatter(x,y, label="mitjanes", color="blue", marker="*", s=30)
plt.xlabel('Restaurants')
plt.ylabel('Mitjanes')
plt.title('Diagrama de dispersió Restaurants')
plt.legend()
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.savefig('../Grafics/diagramaDispersioMitjanaRestaurants.png', bbox_inches='tight')
plt.show()
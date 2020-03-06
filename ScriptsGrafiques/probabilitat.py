import matplotlib.pyplot as plt
import numpy as np

file1 = open('../Resultats/probabilitats.txt', 'r')
Lines = file1.readlines()


probabilitats=[]
puntuacio=[]
for line in Lines:
    if line.split(',')[0] != 'nota':
        probabilitats.append(float(line.split(',')[1]))
        puntuacio.append(float(line.split(',')[0]))

print(probabilitats)
print(puntuacio)
x=range(1, len(puntuacio)+1)

plt.scatter(x, probabilitats)
z = np.polyfit(x, probabilitats, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.savefig('../Grafics/probabilitats.png', bbox_inches='tight')
plt.show()
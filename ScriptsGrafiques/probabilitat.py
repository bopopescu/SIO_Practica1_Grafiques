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

plt.scatter(puntuacio, probabilitats, label="Probabiltat", color="blue", marker="*", s=30)
z = np.polyfit(puntuacio, probabilitats, 1)
p = np.poly1d(z)
plt.plot(puntuacio,p(puntuacio),"r--")
plt.title('Distribució de la Probabilitat')
plt.xlabel('Puntuació')
plt.ylabel('Probabilitat')
plt.legend()
plt.savefig('../Grafics/probabilitats.png', bbox_inches='tight')
plt.show()
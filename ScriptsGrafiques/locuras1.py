import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mysql.connector as mariadb
from scipy import stats
from decimal import *


f = open('../Resultats/mitjanaUsuaris.txt', 'r')
Lines = f.readlines()

mitjana=[]
for line in Lines:
    if line.split(',')[0]!='idUsuari':
        mitjana.append(float(line.split(',')[1]))
mitjanaI=[]
for i in mitjana:
    mitjanaI.append(int(i))

f = open('../Resultats/desviacioESTPOBXUsuari.txt', 'r')
Lines = f.readlines()
desviacio = []
for desvest in Lines:
    desviacio.append(float(desvest.split(',')[1]))

plt.scatter(mitjana, desviacio)
plt.title('Mitjana/Desviacio Usuari')
plt.xlabel('Mitjana')
plt.ylabel('Desviació')
plt.savefig('../Grafics/mitjanaDesviacioUsuaris.png', bbox_inches='tight')
plt.show()

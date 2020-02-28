import matplotlib.pyplot as plt
import numpy as np

file1 = open('../Resultats/totesPuntuacions.txt', 'r')
Lines = file1.readlines()
puntuacions=[]
numPuntuacions=0
for line in Lines:
    puntuacions+=[float(line)]
    numPuntuacions = numPuntuacions+1
x=range(0, numPuntuacions)
plt.plot(x, puntuacions)
plt.xlabel('Numero Puntuacions')
plt.ylabel('Puntuacions')
plt.title('aaa')
plt.show()
#https://www.youtube.com/watch?v=tTm7_fvlDMs
#S'ha de calcular la mitjana (que la tenim)
#s'ha de calcular la desviació estàndard (que la tenim)
#S'ha de calcular el límit màxim (mitjana + desvestp)
#S'ha de calcular el límit mínim (mitjana - desvestp)
#La grafica són unes línies verticals representant el límit max i min i la mitjana
#i es veu a sota la grafica de tots els punts.. i ala aparcao xd
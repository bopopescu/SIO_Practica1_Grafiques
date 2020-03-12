import matplotlib.pyplot as plt
import numpy as np

file1 = open('../Resultats/mitjanaRestaurants.txt', 'r')
Lines = file1.readlines()

mitjanes=[]
x=[]
for line in Lines:
    if line.split(",")[0] != 'idRestaurant':
        x+=[int(line.split(',')[0])]
        mitjanes+=[float(line.split(',')[1])]

file1=open('../Resultats/desviacionsEstandardsPoblacionalsPerRestaurant.txt','r')
Lines = file1.readlines()


desvestp=[]
for line in Lines:
    if line.split(',')[0] != 'idRestaurant':
        desvestp+=[float(line.split(',')[1])]

lim_max=[]
lim_min=[]
i=0
while i<mitjanes.__len__():
    lim_min.append(mitjanes[i]-desvestp[i])
    lim_max.append(mitjanes[i]+desvestp[i])
    i=i+1

plt.plot(x,lim_max, color='green', label='Limit Màxim')
plt.plot(x, lim_min, color='red', label='Limit Mínim')
plt.plot(x, mitjanes, label='Mitjana')
plt.legend()
plt.title('Desviacio/Mitjana')
plt.xlabel('Restaurants')
plt.savefig('../Grafics/MitjanaVSLimInfVSLimSup_Restaurant.png', bbox_inches='tight')
plt.show()


file1=open('../Resultats/puntuacionsXRestaurant.txt','r')
Lines = file1.readlines()

puntuacions=[]
for line in Lines:
    if line.split(",")[0] != 'puntuacions\n':
        primera_part=line.split(',')[0]
        segona_part=line.split(',[')[1]
        segona_part=segona_part.replace(',]','')
        if ']\n' in segona_part:
            segona_part=segona_part.replace(']\n', '')
        ll=list(segona_part.split(','))
        ll1=[]
        for p in ll:
            ll1.append(float(p))
        puntuacions.append(ll1)

j=0
conj_superior=[]
superior=[]
conj_inferior=[]
inferior=[]
conj_entremig=[]
entreMig=[]

for scores in puntuacions:
    for p in scores:
        if p < lim_min[j]:
            inferior.append(p)
        elif p > lim_max[j]:
            superior.append(p)
        elif p >= lim_min[j] and p<=lim_max[j]:
            entreMig.append(p)
    j=j+1
    conj_superior.append(len(superior))
    conj_inferior.append(len(inferior))
    conj_entremig.append(len(entreMig))
    inferior=[]
    superior=[]
    entreMig=[]



plt.bar(x, conj_superior, color=['green'])
plt.xlabel('Identificador de restaurant')
plt.ylabel('Puntuacions')
plt.title('Puntuacions superiors al límit màxim')
plt.savefig('../Grafics/numPpuntuacionsLimitMax.png', bbox_inches='tight')
plt.show()

plt.bar(x, conj_inferior, color=['red'])
plt.xlabel('Identificador de restaurant')
plt.ylabel('Puntuacions')
plt.title('Puntuacions inferiors al límit mínim')
plt.savefig('../Grafics/numPuntuacionsLimitMin.png', bbox_inches='tight')
plt.show()

plt.bar(x, conj_entremig, color=['blue'])
plt.xlabel('Identificador de restaurant')
plt.ylabel('Puntuacions')
plt.title('Puntuacions entre límits')
plt.savefig('../Grafics/numPuntuacionsEntreLimits.png', bbox_inches='tight')
plt.show()
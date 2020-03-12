import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mysql.connector as mariadb
from scipy import stats
from decimal import *

mariadb_connection = mariadb.connect(user='root', password='', database='SIO')
cursor = mariadb_connection.cursor()

puntuacionsDiferents=[]
cursor.execute("SELECT DISTINCT puntuacio FROM relusrrest WHERE (puntuacio!=99.00)")
myresult = cursor.fetchall()
for elem in myresult:
    aux=float(str(elem[0]))
    puntuacionsDiferents.append(aux)
puntuacionsDiferents.sort()
print(puntuacionsDiferents)

puntuacionsXUsuari = []
j = 1
while j <=73421:
    cursor.execute("SELECT puntuacio FROM relusrrest WHERE (usuari="+str(j)+" AND puntuacio!=99.00)")
    myresult = cursor.fetchall()
    ll = []
    for elem in myresult:
        aux = float(str(elem[0]))
        ll.append(aux)
    puntuacionsXUsuari.append(ll)
    print(str(j)+" FET!")
    j = j + 1

print("------CALCULANT LES VEGADES QUE APAREIX CADA VALOR PER CADASCUN DELS USUARIS------")
resG={}
j=1
for llista in puntuacionsXUsuari:
    aux={}
    for p in puntuacionsDiferents:
        if p in llista:
            aux[p]=1
    resG[j]=aux
    print(str(j)+" FET!")
    j=j+1

resultatGlobal={}
for elem in puntuacionsDiferents:
    resultatGlobal[elem] = 0
print(resultatGlobal)
print("resultat global inicitalitzat.")
for key in resG.keys():
    dict_aux = resG[key]
    for key in dict_aux.keys():
        resultatGlobal[key] = resultatGlobal[key] + dict_aux[key]
print(resultatGlobal)

keys = resultatGlobal.keys()
claus =[]
for k in keys:
    claus.append(k)
claus.sort()
vegadesReals = []
for key in claus:
    vegadesReals.append(resultatGlobal[key])
print(vegadesReals)
f = open('../Resultats/probabilitats.txt', 'r')
lines = f.readlines()
prob=[]
for line in lines:
    if line.split(',')[0]!='nota':
        prob.append(float(line.split(',')[1]))

plt.scatter(vegadesReals, prob)
plt.title('Probabilitat VS Vegades reals')
plt.xlabel('Vegades que apareix')
plt.ylabel('Probabilitat')
plt.show()

f1 = open('../Resultats/probabilitats.txt', 'r')
linies = f1.readlines()
prob=[]
for line in linies:
    if line.split(',')[0]!='nota':
        prob.append(float(line.split(',')[1]))
f1 = open('../Resultats/vegadesAparicioPuntuacio.txt', 'r')
linies = f1.readlines()
vegades=[]
for line in linies:
    vegades.append(int(line.split(',')[1]))
plt.scatter(vegades,prob)
plt.title('Probabilitat VS Vegades que apareix')
plt.xlabel('Vegades que apareix la puntuació')
plt.ylabel('Probabilitat')
plt.savefig('../Grafics/ProbabilitatVSVegadesQueApareix.png', bbox_inches='tight')
plt.show()


mariadb_connection = mariadb.connect(user='root', password='', database='SIO')
cursor = mariadb_connection.cursor()

puntuacionsDiferents=[]
cursor.execute("SELECT DISTINCT puntuacio FROM relusrrest WHERE (puntuacio!=99.00)")
myresult = cursor.fetchall()
for elem in myresult:
    puntuacionsDiferents.append(elem)
puntuacionsDiferents.sort()
print(puntuacionsDiferents)


f = open('../Resultats/vegadesAparicioPuntuacio.txt', 'w')
for p in puntuacionsDiferents:
    cursor.execute("SELECT DISTINCT count(usuari) FROM relusrrest WHERE (puntuacio="+str(p[0])+")")
    myresult = cursor.fetchone()
    s=str(p[0])+","+str(myresult[0])
    print(s)
    f.write(s+"\n")


file1=open('../Resultats/mitjanaRestaurants.txt', 'r')
Lines = file1.readlines()
mitjanes = []

for line in Lines:
    if line.split(',')[0]!='idRestaurant':
        aux = line.split(',')[1]
        mitjanes.append(float(aux))
print(mitjanes)
mitjanesI=[]

for mitjana in mitjanes:
    mitjanesI.append(int(mitjana))
print(mitjanesI)
elems=dict((x,mitjanesI.count(x)) for x in set(mitjanesI))
print(elems)
x = []

for key in elems.keys():
    x.append(key)
x.sort()
numMitjanes=[]
for p in x:
    numMitjanes.append(elems[p])

print(x)
print(numMitjanes)

plt.scatter(x, numMitjanes)
plt.title('Numero de mitjanes')
plt.xlabel('Mitjana')
plt.ylabel('Numero de mitjanes')
plt.savefig('../Grafics/numMitjanesRestaurants.png', bbox_inches='tight')
plt.show()


f1 = open('../Resultats/modesXUsuari.txt', 'r')
linies = f1.readlines()
modes = []
for line in linies:
    modes.append(int(line.split(',')[1]))

grupModes=[]
sum=0
i=1
for mode in modes:
    sum=sum+mode
    if i == 10000:
        grupModes.append(sum/10000)
        sum=0
        i=0
    i=i+1

f2 = open('../Resultats/mitjanaUsuaris.txt', 'r')
linies = f2.readlines()
mitjanes=[]
for line in linies:
    if line.split(',')[0]!='idUsuari':
        aux = line.split(',')[1]
        mitjanes.append(float(aux))
print(mitjanes)
mitjanesI=[]

for mitjana in mitjanes:
    mitjanesI.append(int(mitjana))

grupMitjanes=[]

sum=0
i=1
for mitja in mitjanesI:
    sum=sum+mitja
    if i == 10000:
        grupMitjanes.append(sum/10000)
        sum=0
        i=0
    i=i+1


plt.scatter(grupMitjanes,grupModes)
plt.title('Relació mitjanes/moda Usuaris')
plt.xlabel('Mitjana')
plt.ylabel('Moda')
z = np.polyfit(grupMitjanes, grupModes, 1)
p = np.poly1d(z)
plt.plot(grupMitjanes,p(grupMitjanes),"r--")
plt.savefig('../Grafics/RelMitjanaModaUsuaris.png', bbox_inches='tight')
plt.show()


file1=open('../Resultats/modaIVegadesUsuaris.txt', 'r')
Lines = file1.readlines()

modes=[]
for line in Lines:
    modes.append(int(line.split(',')[1]))

elems=dict((x,modes.count(x)) for x in set(modes))
print(elems)
vals=[]
x=[]
for key in elems.keys():
    x.append(key)
x.sort()
print(x)
for key in x:
    vals.append(elems[key])
print(vals)
plt.bar(x, vals)
plt.title('Puntuacio mes repetida Usuaris')
plt.xlabel('Mitjana')
plt.ylabel('Vegades visitat')
plt.savefig('../Grafics/PuntuacioMesRepetidaUsuaris.png', bbox_inches='tight')
plt.show()
file1=open('../Resultats/modaIVegadesRestaurants.txt','r')
Lines=file1.readlines()

modes=[]
for line in Lines:
    modes.append(int(line.split(',')[1]))

elems1=dict((x,modes.count(x)) for x in set(modes))
print(elems1)

vals=[]
x=[]
for key in elems1.keys():
    x.append(key)
x.sort()
print(x)
for key in x:
    vals.append(elems1[key])
print(vals)
plt.bar(x, vals)
plt.title('Puntuacio mes repetida Restaurants')
plt.xlabel('Mitjana')
plt.ylabel('Vegades visitat')
plt.savefig('../Grafics/PuntuacioMesRepetidaRestaurants.png', bbox_inches='tight')
plt.show()


mariadb_connection = mariadb.connect(user='root', password='', database='SIO')
cursor = mariadb_connection.cursor()
j=1
f=open('../Resultats/modaIVegadesRestaurants.txt', 'w')
while j<=100:
    cursor.execute("SELECT puntuacio FROM relusrrest WHERE (restaurant="+str(j)+" AND puntuacio!=99.00)")
    myresult = cursor.fetchall()
    ll =[]
    for i in myresult:
        ll.append(i[0])

    moda=stats.mode(ll)
    mode=int(moda.mode)
    counts = moda.count[0]
    s=str(j)+","+str(mode)+","+str(counts)
    print(s)
    f.write(s+"\n")
    j=j+1

file1 = open('../Resultats/mitjanaRestaurants.txt', 'r')
Lines = file1.readlines()

mitjanes = []

for line in Lines:
    if line.split(',')[0]!='idRestaurant':
        mitjanes.append(float(line.split(',')[1]))

file1 = open('../Resultats/desviacioESTPOBXRestaurant.txt', 'r')
Lines=file1.readlines()

desvestp =[]
for line in Lines:
    desvestp.append(float(line.split(',')[1]))

plt.scatter(mitjanes, desvestp)
plt.title('Mitjana/desviacio')
plt.savefig('../Grafics/mitjanaDesviacioRestaurants.png', bbox_inches='tight')
plt.show()


file1= open('../Resultats/desviacioESTPOBXUsuari.txt', 'r')
Lines = file1.readlines()

desvestp=[]
for line in Lines:
    desvestp.append(float(line.split(',')[1]))

file1 = open('../Resultats/mitjanaUsuaris.txt', 'r')
Lines = file1.readlines()
mitjanes=[]
for line in Lines:
    if line.split(',')[0] != 'idUsuari':
        mitjanes.append(float(line.split(',')[1]))

plt.scatter(mitjanes, desvestp)
plt.title('Mitjana/desviacio')
plt.savefig('../Grafics/mitjanaDesviacioUsuaris.png', bbox_inches='tight')
plt.show()


file1 = open('../Resultats/visitatsXUsuari.txt', 'r')
Lines = file1.readlines()

usuari=[]
visitats=[]
for line in Lines:
    usuari.append(int(line.split(',')[0]))
    visitats.append(int(line.split(',')[1]))

file1 = open('../Resultats/mitjanaUsuaris.txt', 'r')
Lines = file1.readlines()

mitjanaUsuaris = []
for line in Lines:
    if line.split(',')[0]!='idUsuari':
        mitjanaUsuaris.append(float(line.split(',')[1]))



plt.title('Relació mitjana/visitats')
z = np.polyfit(mitjanaUsuaris, visitats, 1)
p = np.poly1d(z)
plt.scatter(mitjanaUsuaris, visitats)
plt.plot(mitjanaUsuaris, p(mitjanaUsuaris), "r--")
plt.savefig('../Grafics/relacioMitjanaVisitatsUsuaris.png', bbox_inches='tight')
plt.show()
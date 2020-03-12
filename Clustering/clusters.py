import mysql.connector as mariadb
from sklearn.cluster import KMeans
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from Clustering.RelRestMitj import RelRestMitj

mariadb_connection = mariadb.connect(user='root', password='', database='SIO')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT DISTINCT puntuacio FROM relusrrest WHERE puntuacio!=99.00")
myresult = cursor.fetchall()
ll =[]
for i in myresult:
    ll.append(i[0])
ll.sort()
for elem in ll:
    print(str(elem))


"""
mitjanes_x=[]
rest_visitats_y=[]
for i in range(1,3): #range(1,101)!
    cursor.execute("SELECT AVG(puntuacio) AS mitjana FROM relusrrest WHERE (puntuacio!=99.00 AND restaurant="+str(i)+")")
    myresult = cursor.fetchone()
    mitjanes_x.append(myresult[0])
    cursor.execute("SELECT count(puntuacio) AS influenciaGent FROM relusrrest WHERE(puntuacio!=99.00 AND restaurant="+str(i)+")")
    myresult = cursor.fetchone()
    rest_visitats_y.append(myresult[0])

dict={}
dict['x'] = mitjanes_x
dict['y'] = rest_visitats_y


df = DataFrame(dict, columns=['x', 'y'])
df['id'] = df.index
print(df)
kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)"""
#plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)







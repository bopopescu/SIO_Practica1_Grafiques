import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


activities = ['Aprobats', 'Suspesos']
slices=[70,30]
colors=['g', 'r']
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0.1,0), radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.title('Percentatge de restaurants Aprobats/Suspesos')
plt.savefig('../Grafics/restaurantsAprobatsSuspesos.png', bbox_inches='tight')
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

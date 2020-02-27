import matplotlib.pyplot as plt

activities = ['Aprobats', 'Suspesos']
slices=[70,30]
colors=['g', 'r']
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0.1,0), radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.title('Percentatge de restaurants Aprobats/Suspesos')
plt.savefig('../Grafics/restaurantsAprobatsSuspesos.png', bbox_inches='tight')
plt.show()
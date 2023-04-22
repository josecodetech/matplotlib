import matplotlib.pyplot as plt
import pandas as pd

# Leer el conjunto de datos de propinas desde la URL
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
datos_propinas = pd.read_csv(url)

# Crear mapa de calor de correlación de las variables
correlacion = datos_propinas.corr()
plt.imshow(correlacion, cmap='coolwarm')
plt.colorbar()
plt.xticks(ticks=range(len(correlacion.columns)),
           labels=correlacion.columns, rotation=90)
plt.yticks(ticks=range(len(correlacion.columns)), labels=correlacion.columns)
plt.title('Mapa de calor de correlación')

# Mostrar gráfico
plt.show()

# Crear gráfica de puntos de las propinas por total de la cuenta
plt.scatter(datos_propinas['total_bill'], datos_propinas['tip'])
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.title('Propinas por total de la cuenta')

# Mostrar gráfico
plt.show()

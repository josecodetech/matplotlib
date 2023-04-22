import matplotlib.pyplot as plt
import numpy as np

# Crear datos de prueba de ventas
# Distribución normal con media de 50000 y desviación estándar de 15000
ventas = np.random.normal(50000, 15000, 1000)

# Crear histograma
# Crear histograma con 30 bins y borde negro
plt.hist(ventas, bins=30, edgecolor='black')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.title('Histograma de Ventas')

# Mostrar gráfico
plt.show()

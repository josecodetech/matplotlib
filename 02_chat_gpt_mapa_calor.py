import matplotlib.pyplot as plt
import numpy as np

# Crear datos de prueba
datos = np.random.rand(10, 10)  # Matriz de 10x10 con valores aleatorios

# Crear mapa de calor
plt.imshow(datos, cmap='coolwarm')  # Utilizar el mapa de colores "coolwarm"
plt.colorbar()  # Agregar una barra de color para indicar la escala
plt.title('Mapa de Calor')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar gráfico
plt.show()

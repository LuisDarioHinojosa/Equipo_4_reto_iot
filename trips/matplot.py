import matplotlib.pyplot as plt
import random

datos = [random.randint(50, 100) for num in range(1000)]


plt.plot(datos)

plt.show()

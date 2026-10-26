import matplotlib.pyplot as plit 
import numpy as np
print("Christian Garcia Jimenez Nc= 0068")

num_mes = np.array([1, 2, 3, 4, 5, 6])
venta_manda2 = np.array([0, 2000, 3500, 7000, 15000, 20000])

plit.plot(
    num_mes, 
    venta_manda2,
    marker="*",
    markersize=10,
    markerfacecolor="#f54927",
    markeredgecolor="blue"
)

plit.show()
print("Christian Garcia Jimenez Nc= 0068")
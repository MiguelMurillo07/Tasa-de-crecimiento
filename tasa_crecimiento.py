# Ejercicio #28: En 1980 la ciudad A tenia 3.5 millones de habitantes y una rata de crecimiento del 7% anual; si la ciudad B tenía 5 millones y una rata de crecimiento del 5% anual. Si el crecimiento poblacional se mantiene constante en las 2 ciudades, hacer el diagrama de flujo y programa en Python que calcule e imprima en que año la poblacion de la ciudad A es mayor que la de la ciudad B.


print("---------------------------------------")
print("----------Tasa de Crecimiento----------")
print("---------------------------------------")

# input

A = 3500000
B = 5000000
y = 1980

# processing

while A<=B:
    A=A+(A*0.07)
    B=B+(B*0.05)
    y=y+1

print("El año en que la poblacion A sera mayor que la B es en " +str(y))
for i in range(100) :
    print(i+1)

for i in range (2, 8):
    print("El valor de i es actualmente", i)

for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)

import time
    # Escribe un ciclo for que cuente hasta cinco.
    # Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    # Cuerpo del ciclo - uso: time.sleep (1)
for i in range(5) :
    print(i+1,'Mississippi')
    time.sleep(1)
# Escribe una función de impresión con el mensaje final.
print('Listo o no , ahí voy')
# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

for i in range(0,20,2) :
    print(i)

#  Accidentalmente, logré uno que me entrega los números impares
for i in range(0,20,2) :
    print(i+1)

# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")
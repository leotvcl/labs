def displayTitle() :
    print(
        """
        +==================================+
        | Bienvenido a mi juego, muggle!   |
        | Introduce un número entero       |
        | y adivina qué número he          |
        | elegido para ti.                 |
        | Entonces,                        |
        | ¿Cuál es el número secreto?      |
        +==================================+
        """)


displayTitle()
numeroSecreto = 777

while numeroSecreto :
    try:
        numeroSecreto = int(input("Ingresa tu número secreto: "))    
        if numeroSecreto != 777 :
            print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
        else :
            break
    except: 
        print("¡Te crees Listo eh!, ingresa un número")
print("¡Bien hecho muggle!, eres libre ahora ")
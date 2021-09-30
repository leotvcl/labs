###  Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto
###  o común . Los primeros tienen una duración de 366 días, mientras que los últimos tienen
###  una duración de 365 días.
###  Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla
###  para determinar el tipo de año:
###  Si el número del año no es divisible entre cuatro, es un año común.
###  De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
###  De lo contrario, si el número del año no es divisible entre 400, es un año común.
###  De lo contrario, es un año bisiesto.
def determiningTypeOfYear(year) :
    x = year % 4
    if year >= 1582 and x != 0:
        print("Año Común")
    elif year >= 1582 and x == 0 :
        print("Año Bisiesto")
    elif year < 1582 :
        print("Año fuera de norma")
    return(year)
try: 
    year = int(input("Introduzca un año:"))
    determiningTypeOfYear(year)

except :
    print("Al parecer no ingresaste un año en números")

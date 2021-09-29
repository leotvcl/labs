def pairOrOdd(number) :
    number %= 2
    if number == 0 :
        print("El número es Par")
    else :
        print("El número es Impar")
    return number

try :
    number = int(input("Por favor ingrese un número: "))
    pairOrOdd(number)
except:
    print("Parece que no ingresaste un número")


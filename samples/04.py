def espatifilo(flower) :
    if flower == "Espatifilo" :
        print("Sí, ¡El espatifilo es la mejor planta de todos los tiempos")
    elif flower == "espatifilo" :
        print("No, ¡quiero un gran Espatifilo!")
    else :
        print("¡Espatifilo! ¡No",flower,"!")

flower = input("Ingrese el nombre de una planta: ")
espatifilo(flower)

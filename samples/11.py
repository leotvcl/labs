phrase = "chupacabra"
while phrase :
    
    phrase = input("Ingrese frase de paso: ")
    if phrase == "chupacabra" : break
    
print("¡Has salido del ciclo!")

#  Me como las vocales 

userWord = input("Ingrese una palara (me comeré las vocales): ")
userWord = userWord.upper()
for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra != "A" and letra !="E" and letra !="I" and letra !="O" and letra !="U" :
        print(letra)
#  Author: Leonardo Trincado
#  Date: 24/10/2021
#  Testing functions and best practices 

if __name__ == '__main__' :
          
    def printGreeting(name) :
        print("Hola", name)
         
    def printErrorMessage() :
        print("¡Tuvimos un error!")

    try :
        name = input("Ingrese su nombre: ")
        printGreeting(name)
    except :
        printErrorMessage()

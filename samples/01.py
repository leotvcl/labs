def evaluate_is_String(chainString) :
    validate = chainString.isdigit()
    return validate

def validate_long_String(chainString) :
    large = len(chainString)
    return large

def putTitle(chainString) :
    chainString = chainString.title()
    return chainString

def errorMessage() :
    print("Parece que no ingresaste un valor correctamente")

fruit_list = []
answer = "s"

while answer == "s" :
    try :
        fruit = input("Por favor ingresa una fruta: ")       
        if evaluate_is_String(fruit) == False and validate_long_String(fruit) >= 4:
            fruit_list.append(putTitle(fruit))
        else :
            errorMessage()
    except:
        errorMessage()
    
    try :
        answer = input("Desea seguir ingresando frutas s = Sí / n = No ")
        answer.lower()
    except:
        errorMessage()

if len(fruit_list) > 0 :
    print("Tus frutas ingresadas fueron:  \n", fruit_list)
else :
    errorMessage()
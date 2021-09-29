def taxCalculator(ingreso):
    if ingreso < 85528 and ingreso > 0 :
        impuesto = (ingreso * 0.18) - 556.2
    if ingreso > 85528 :
        impuesto = ((ingreso - 85528) * 0.32)  + 14839
    if ingreso <= 0 :
        impuesto = 0.0
    impuesto=round(impuesto, 0)
    return impuesto

try:
    ingreso=float(input("Ingrese el ingreso anual:"))
    impuesto = taxCalculator(ingreso)
    print("El impuesto es: ", impuesto, "pesos")

except:
    print("Tuvimos un error")
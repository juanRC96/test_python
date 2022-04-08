def suma(n1,n2):
    return (n1+n2)

def resta(n1,n2):
    return (n1-n2)

operacion = input("Ingrese una operacion a realizar 1:Suma, 2:Resta")

if operacion in ('1','2'):
    n1 = float(input("Ingrese el primer valor: "))
    n2 = float(input("Ingrese el segundo valor: "))

if operacion == '1':
    print("La suma es ",suma(n1,n2))

elif operacion == '2':
    print("La resta es ",resta(n1,n2))

#PEDIR NUMEROS HASTA QUE SE INGRESE UN NUMERO NEGATIVO
while True:
    num = int(input("Ingresa un numero :"))
    if num < 0:
        print("Termino el programa")
        break

#PEDIR 5 NUMEROS Y GUARDARLOS EN UNA LISTA E IMPRIMIR LA SUMA Y EL PROMEDIO
numeros = []
for i in range(5):
    num = float(input(f"Ingresa un número: "))
    numeros.append(num)

suma = sum(numeros)
promedio = suma / len(numeros)

print(f"Suma de los nUmeros: {suma}")
print(f"Promedio de los nUmeros: {promedio}")
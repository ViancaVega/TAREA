#crea una función multiplicar_matrices(A, B) que reciba 
# dos matrices (listas de listas) y devuelva su producto
# consideraciones:

#validar que el número de columnas de A sea igual al número de filas de B
#usar ciclos anidados para recorrer filas y columnas
#devolver la matriz resultante
def pedir(nom):
    fi = int(input(f"¿cuantas filas tiene la matriz {nom}? ="))
    col = int(input(f"¿cuantas columnas tiene la matriz {nom}? ="))
    matriz = []

    print(f"ingrese los valores de la matriz {nom} fila por fila :")
    for i in range(fi):
        fi= input(f"Fila {i + 1}: ")
        num = list(map(int, fi.strip().split()))
        while len(num) != col:
            print(f"La fila debe tener exactamente {col} numeros")
            fi = input(f"Fila {i + 1} nuevamente: ")
            num = list(map(int, fi.strip().split()))
        matriz.append(num)
    
    return matriz
def multiplicar(A, B):
    if len(A[0]) != len(B):
        return "no se pueden multiplicar las matrices:"

    res = [[0 for _ in range(len(B[0]))]  for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]

    return res

print("matriz A:")
A = pedir("A")
print("\nmatriz B:")
B = pedir("B")

print("\nresultado :")
res = multiplicar(A, B)

if isinstance(res,  str):
    print(res)
else:
    for fila in res:
        print(fila)
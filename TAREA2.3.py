#CREAR UNA FUNCION QUE RECIBA UN NUMERO Y RETORNE SI ES PRIMO O NO
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingresa un número:"))

if es_primo(numero):
    print(f"{numero} es un numero primo")
else:
    print(f"{numero} no es un numero primo")

#crea una clase CuentaBancaria que tenga:
#atributos: titular, saldo
#métodos: depositar(monto), retirar(monto), mostrar_saldo()
#requisitos:
#no permitir retiros mayores al saldo disponible.
#mostrar advertencia si se intenta retirar más dinero del que hay disponible.
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"depósito exitoso. nuevo saldo: {self.saldo}")
        else:
            print("el monto a depositar debe ser positivo")

    def retirar(self, monto):
        if monto > self.saldo:
            print("no se puede retirar más dinero del disponible")
        elif monto <= 0:
            print("el monto a retirar debe ser positivo")
        else:
            self.saldo -= monto
            print(f"retiro exitoso. nuevo saldo: {self.saldo}")

    def mostrar_saldo(self):
        print(f"saldo actual de {self.titular}: {self.saldo}")


cuenta = CuentaBancaria("Vianca", 1500)
cuenta.mostrar_saldo()
cuenta.depositar(500) 
cuenta.retirar(200)
cuenta.retirar(2000)  
cuenta.mostrar_saldo()
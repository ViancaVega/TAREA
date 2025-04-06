#crea una clase Estudiante que tenga:
#atributos: nombre, lista de notas
#metodos: agregar_nota(), promedio(), mostrar_informacion()

#ejemplo de uso:
#e1 = Estudiante("Carlos")
#e1.agregar_nota(80)
#e1.agregar_nota(95)
#e1.promedio() 
#devuelve 87.5
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.promedio():.2f}")

e1 = Estudiante("Carlos")
e1.agregar_nota(80)
e1.agregar_nota(95)
e1.mostrar()
e2 = Estudiante("Luis")
e2.agregar_nota(50)
e2.agregar_nota(60)
e2.mostrar()
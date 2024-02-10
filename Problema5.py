class Alumno:
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Nombre:", self.nombre)
        print("Número de registro:", self.num_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No asignada")
        if self.notas:
            print("Notas:", ", ".join(map(str, self.notas)))
        else:
            print("Notas: No asignadas")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.notas.append(nota)

alumno1 = Alumno("Juan", 12345)
alumno1.setAge(20)
alumno1.setNota(80)
alumno1.setNota(75)
alumno1.display()

class Libro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.estudiantes = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, codigo):
        for libro in self.libros:
            if libro.isbn == codigo:
                self.libros.remove(libro)
                return
        print("Libro no encontrado")

    def listar_libros(self):
        for libro in self.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Codigo: {libro.codigo}")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, numero_estudiante):
        for estudiante in self.estudiantes:
            if estudiante.numero_estudiante == numero_estudiante:
                self.estudiantes.remove(estudiante)
                return
        print("Estudiante no encontrado")

    def listar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(f"Nombre: {estudiante.nombre}, Número de estudiante: {estudiante.numero_estudiante}")

class Estudiante:
    def __init__(self, nombre, numero_estudiante):
        self.nombre = nombre
        self.numero_estudiante = numero_estudiante

# Ejemplo de uso:
        

biblioteca = Biblioteca()

libro1 = Libro("Don Quijote", "Miguel de Cervantes", "978-84")
libro2 = Libro("1984", "George Orwell", "206-0290")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

estudiante1 = Estudiante("Juan Pérez", 123)
estudiante2 = Estudiante("Ana García", 678)

biblioteca.agregar_estudiante(estudiante1)
biblioteca.agregar_estudiante(estudiante2)

biblioteca.listar_libros()
biblioteca.listar_estudiantes()
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"Este es un {self.marca} {self.modelo} del año {self.año}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas

    def descripcion(self):
        return f"Este es un {self.marca} {self.modelo} del año {self.año} con {self.numero_puertas} puertas"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_bicicleta):
        super().__init__(marca, modelo, año)
        self.tipo_bicicleta = tipo_bicicleta

    def descripcion(self):
        return f"Esta es una {self.marca} {self.modelo} del año {self.año}, una bicicleta de {self.tipo_bicicleta}"

# Ejemplo de uso:
mi_coche = Coche("Toyota", "Corolla", 2023, 4)
mi_bicicleta = Bicicleta("Trek", "Madone", 2022, "carretera")

print(mi_coche.descripcion())
print(mi_bicicleta.descripcion())
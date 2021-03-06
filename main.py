class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color 
        self.precio = precio
        self.registro = registro
    def cambiarColor(self,color):
        lista_colores = ["verde", "rojo", "amarillo", "negro", "blanco"]
        if color in lista_colores:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        lista_tipo = ["gasolina","electrico"]
        if tipo in lista_tipo:
            self.tipo = tipo

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        a = 0
        for e in self.asientos:
            if e != None:
                a += 1
        return a
    def verificarIntegridad(self):
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        for e in self.asientos:
            if e != None:
                if e.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"
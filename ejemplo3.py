argentina={
    "portero":"joselito",
    "defensas":["pasarela","el otro", "el de la moto"],
    "medios":False,
    "delanteros":"maradona"
}
brasil={
    "portero":"fulanito",
    "defensas":["roberto carlos","marcelo", "otro"],
    "medios":"zico",
    "delanteros":"ronaldo el rodillas"
}
class Pais:
    def __init__(self, nombre, capital):
        self.nombre=nombre
        self.capital=capital
class Coche:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
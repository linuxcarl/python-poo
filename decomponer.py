class Automovil:
    
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)

    def encender(self, tipo="electrico"):
        self._motor.encender(tipo)
        
    def arrancar(self, inicio="despacio"):
        self.inicio = inicio

class Motor:
    
    def __init__(self, cilindros, tipo = 'gasolina' ):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def encender(self,tipo="gasolina", cantidad=0):
        pass
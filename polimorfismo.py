class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'{self.nombre} camina por favor')

class Ciclista(Persona):
    
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print(f'{self.nombre} avanza en tu bici por favor')

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__ == '__main__':
    main()
    
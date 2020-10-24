class Coordenada:
    
    def __init__(self, x, y ):
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        x_diff = (self.x - otra_cordenada.x)**2
        y_diff = (self.y - otra_cordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordenada(10,5)
    corde_2 = Coordenada(8,4)

    print(coord_1.distancia(corde_2))
    print(isinstance(corde_2, Coordenada))
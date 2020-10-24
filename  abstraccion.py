class Lavasecadora:

    
    def __init__(self):
        pass

    def lavar(self, temperatura = 'caliente', secado=False):
        self._llenar_tanque_de_agua(temperatura)
        self._agregar_jabon()
        self._lavar()
        self._sentrifugar()
        if secado:
            self._secar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _agregar_jabon(self):
        print('Agregando jabon...')

    def _lavar(self):
        print('Lavando...')

    def _sentrifugar(self):
        print('Sentrifugando....')

    def _secar(self):
        print('Secando ropa...')    

if __name__ == "__main__":
    lavadora = Lavasecadora()
    lavadora.lavar(secado=True)
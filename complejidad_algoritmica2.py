import time
import math


class ComplejidadAlgoritmica:
    
    def __init__(self, number):
        self.number = number
    #O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
    def constante(self):
        return self.number
    #O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
    def logaritmica(self):
        return math.log10(self.number)
    #O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
    def lineal(self):
        return self.number
    #O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
    def log_lineal(self):
        return self.number * math.log10(self.number)
    #O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
    def polinominal(self):
        return self.number**2
    #O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
    def exponencial(self):
        return 2**self.number

def main():
    nums = [1,5,10,15,20,30,100,1000,10000]

    for n in nums:
        
        complejidad = ComplejidadAlgoritmica(n)
        
        print('n es igual a: {}'.format(n))
        principio = time.time()
        print(f'El resultado de complejidad constante para n igual a {n} es: ', complejidad.constante())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica para n igual a {n} es: ', complejidad.logaritmica())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad lineal para n igual a {n} es: ', complejidad.lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica lineal para n igual a {n} es: ', complejidad.log_lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad polinominal para n igual a {n} es: ', complejidad.polinominal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
       
       
        principio = time.time()
        print(f'El resultado de complejidad exponencial para n igual a {n} es: ', complejidad.exponencial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        print('\n\n')
        

if __name__ == '__main__':
    
    main()
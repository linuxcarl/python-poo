import time
import math


class ComplejidadAlgoritmica:
    
    def __init__(self, number):
        self.number = number

    def constante(self):
        return self.number

    def logaritmica(self):
        return math.log10(self.number)

    def lineal(self):
        return self.number
    
    def log_lineal(self):
        return self.number * math.log10(self.number)

    def polinominal(self):
        return self.number**2
    
    def exponencial(self):
        return 2**self.number

def main():
    nums = [1,5,10,15,20,30,100,1000,1000000000]

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
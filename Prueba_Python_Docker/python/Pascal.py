'''
Created on 14 abr. 2019

@author: cristian    
'''

import math
from decimal import Decimal 


def pascal(num1, num2):  
    """Pascal : Encuentra los valores no divisibles por 7 dentro del triangulo pascal.
        Variables:
        c_(nr) : Numero combinatorio
        n : Numero variable infinito 
        m : Numero variable infinito
        n!: Numero factorial de n
        m!: Numero factorial de m
    
    Formula:
        c_(mn)=(m!)/(n!(m-n)!)=(m; n), 

    
    Parametros:
        num1 -- valor numerico base
        num2 -- valor numerico exponencial
    

    Excepciones:
        ValueError -- Si (a == 0)   

    """
    qFilas = pow(num1, num2)  # Exponente
    n = 0; m = 0; qEntradas = 0; qModSiete = 0; salida = 0
    
    while (n <= (qFilas - 1)):
    
        while (m <= n):
            salida = int (Decimal(math.factorial(n)) / Decimal(math.factorial(m) * math.factorial(n - m)))
            if (salida % 7) == 0 :
                qModSiete += 1
            else:   
                archivo = open('prueba.log', 'a')
                archivo.write(str(salida)+'\n')
                archivo.close()
            
            qEntradas += 1
            m += 1
            
        n += 1
        m = 0
    
    print('\n\n Total entradas: ', qEntradas,
          '\n Total filas: ', qFilas,
          '\n Total entradas divisibles por siete: ', qModSiete,
          '\n Total entradas no divisibles por siete: ', qEntradas - qModSiete, '\n')

    
pascal(10, 9)


'''
Created on 14 abr. 2019

@author: cristian    
'''


def fibonacci(num1):  
    """Fibonacci : Suceccion infinita de numeros naturales.
        Variables:
        k1 : indice donde estan en los primeros 9 
        k2 : indice donde estan en los ultimos 9 
        k3 : indice donde estan en los primeros 9 digitos y en los ultimos 9 digitos
        a : valor final
        b : valor inicial
        c : acumulador
    
    Formula: 
        Fn = Fn−1 + Fn−2, donde F1 = 1 y F2 = 1 
    
    Parametros:
        num1 -- valor numerico limite 'maximo' de la serie
    
    """
    
    k1 = 0; k2 = 0; k3 = 0;  i = 0; a = 0; b = 1; c = 0
   
    for i in range (num1):
        
        
        
        if(i < num1):
            
            x = str(a)
                   
            print(str(a))
            
            c = a + b
            a = b
            b = c
            
        else:
            x = str(a)
            print(str(a))
            
        j = 0
        suma = 0
        lista1 =[]
        for j in range (len(x[:9])) : 
            lista1.append(int(x[j:j + 1]))
            suma += int(x[j:j + 1])
            if (suma == 45 and (lista1.count(1)==1) and (lista1.count(2)==1) and (lista1.count(3)==1) and (lista1.count(4)==1) and (lista1.count(5)==1) and (lista1.count(6)==1) and (lista1.count(7)==1) and (lista1.count(8)==1) and (lista1.count(9)==1)):
                
                if(k1==0):
                    k1 = i
        j = 0
        suma = 0        
        lista2 =[]
        for j in range (len(x[:9])) : 
            lista2.append(int(x[len(x)-(j+1):len(x)-j]))
            suma += int(x[len(x)-(j+1):len(x)-j])
            if (suma == 45 and (lista2.count(1)==1) and (lista2.count(2)==1) and (lista2.count(3)==1) and (lista2.count(4)==1) and (lista2.count(5)==1) and (lista2.count(6)==1) and (lista2.count(7)==1) and (lista2.count(8)==1) and (lista2.count(9)==1)):
                
                if(k2==0):
                    k2 = i
        
        j = 0
        suma1 = 0
        suma2 = 0 
        lista1 =[]
        lista2 =[]
        for j in range (len(x[:9])) : 
            lista1.append(int(x[j:j + 1]))
            suma1 += int(x[j:j + 1])
            lista2.append(int(x[len(x)-(j+1):len(x)-j]))
            suma2 += int(x[len(x)-(j+1):len(x)-j])
            if (suma1 == 45 and (lista1.count(1)==1) and (lista1.count(2)==1) and (lista1.count(3)==1) and (lista1.count(4)==1) and (lista1.count(5)==1) and (lista1.count(6)==1) and (lista1.count(7)==1) and (lista1.count(8)==1) and (lista1.count(9)==1) and suma2 == 45 and (lista2.count(1)==1) and (lista2.count(2)==1) and (lista2.count(3)==1) and (lista2.count(4)==1) and (lista2.count(5)==1) and (lista2.count(6)==1) and (lista2.count(7)==1) and (lista2.count(8)==1) and (lista2.count(9)==1)):
            
                if(k3==0):
                    k3 = i
        
    print('\nEl indice donde estan en los primeros 9 digitos los numeros del 1-9 es: '+str(k1))  # indice del k
    print('\nEl indice donde estan en los ultimos 9 digitos los numeros del 1-9 es: '+str(k2))  # indice del k
    print('\nEl indice donde estan en los primeros 9 digitos y en los ultimos 9 digitos es los numeros del 1-9 es: '+str(k3))  # indice del k
          
    

fibonacci(900000)


#============================================
#uso de reducciones (colapsar resultados)
#============================================

#============================================
#multiplicacion de todos los numeros en la lista
#============================================

from functools import reduce
bigdata = [2,3,5,7,11,13,19,23,29]

#============================================
#funcion x*y
#============================================
multiplicar = lambda x,y : x*y
print(reduce(multiplicar, bigdata))

#============================================
#reduce le aplica la funcion por pares a los resultados y
#el siguiente elemento comenzando con los dos primeros
#elementos
#============================================

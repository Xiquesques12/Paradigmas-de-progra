#============================================
#uso de filtros
#============================================

#============================================
#hacer una lista de los numeros por arriba del promedio
#============================================

#modulo de estadistica
import statistics
bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#============================================
#hazme una lista de elementos que cumplan la condicion x> promedio
#filter(condicion, datos)
#============================================
print(list(filter(lambda x: x> promedio, bigdata)))

#============================================
#limpiar datos
#============================================
paises = ["","Argentina","","brasil","","Chile","Mexico","","colombia","","","cuba","Venezuela"]
#============================================
#Filtra lo que no contiene nada
#============================================
print(list(filter(None, paises)))

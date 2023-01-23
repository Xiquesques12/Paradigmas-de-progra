#==================================
# conjunto en python
#==================================
even_nums = {2,4,6,8,10} #conjunto de numeros pares
print(even_nums)

#El bool no es parte del conjunto
emp = {1,'xiques',True, 10.5} #conjuntos de diferentes objetos y diferente tipo 
print(emp)
nums = {1,2,2,3,4,4,5,5}
print(nums)
#=======================================
#convertir secuencia a conjunto
#no lo genera en orden
#=======================================
s = set('hello')
print(s)
s= set((1,2,3,4,5)) #tupla a conjunto
print(s)

#================================================
# de diccionario a conjunto: conjunto de llaves
#================================================
d = {1:'one', 2:'two'}
s = set(d)
print(s)
s.add(100)
print(s)
s.update(nums)
print(s)



s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 #union
print(su)

si= s1&s2   #interseccion
print(si)
sr= s1-s2 #diferencia de conjuntos
sp = s2-s1
print(sr)
print(sp)

ss= s1^s2 #diferencia simetrica
print(ss)

#===============================================
#uso de diccionarios
#===============================================
capitals = {"USA": "Washigton D.C", "FRANCE":"Paris", "India":"New Delhi"}
print(capitals)

#================================================
#llave: valor
#=================================================
#diccionario vacio
d={}

#llave entera, valor string
numNames={1:"one", 2:"two",3:"three"}
#llave real, valor string
decnames={1.5:"one and half",2.5:"two and half",3.5:"three and half"}
#llave tupla, valor string
items = {("parker","reynolds","camlin"):"pen",("LG","whirpool","samsung"):"refrigerator"}
#llave string, valor int
romanNums={'I':1, 'II': 2,'III': 3,'IV': 4,'V': 5}
print(romanNums)
print(romanNums['I'])
print(capitals.get("India"))
print(capitals.get('india'))

#reportar llave y valor
for k in capitals:
    print("key = "+ k +", value = "+ capitals[k])
#Nuevo dato para el diccionario
capitals["mexico"] = "cdmx"
print(capitals)
#borrar dato del diccionario
del capitals["mexico"]
print(capitals)
#borrar todo el diccionario
del capitals
#reportar llaves
print(romanNums.keys())
#reportar valores
print(romanNums.values())
#juicio de llave (está o no está la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX"in romanNums )

#========================================
#Listas
#Las listas pueden ser de objetos diferentes
#========================================
miprimeralista= [] #lista vacia
print(miprimeralista)

#=========================================
#llenado de lista
#========================================
miprimeralista = [1,"javier",1.34,"bosco", "angel", True]
print(miprimeralista)

#=========================================
#list: hacer una lista
#range(i,j): secuencia de i hasta j
#========================================
nums2= list(range(1,61))
for i in nums2:
    print(i)
#===========================================
#incluir nuevos elementos en la lista
#===========================================
nums2.append(61)
nums2.append(62)
nums2.append(61)
print(nums2)

#==============================================
#quitar elementos de la lista
#===========================================
nums2.remove(61)
print(nums2)
#===========================================
#quitar elemento con indice i
#==========================================
i=61
del nums2[i]
print(nums2)
#=========================================
#borrar lista
#======================================
del nums2
#========================================
#sumar listas
#=======================================
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)
#=====================================
#llenado a mano
#===================================
potencial = []
for i in range (0,10000):
    potencial.append(float(i))
print(potencial[100])
#======================================
#generar tupla con la lista
#======================================
potencial= tuple(potencial)
print(potencial[100])
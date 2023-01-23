#============================================
# Funcion pura x**2
#============================================
def alcuadrado(x):
    return x*x
#============================================
#funcion pura x**3
#============================================
def alcubo(x):
    return x*x*x
#============================================
#Mapeo de una funcion pura
#============================================
def mapeo(func,lista_numeros):
    resultado = []

    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo(alcuadrado,[2.5,2,3.8,1.2,6.6,1j,7,8])
cubos = mapeo(alcubo,[1,2,3,4,5,6,7,8])
print(cuadrados)
print(cubos)

#============================================
#funciones dentro de funciones
#============================================
def en_mayusculas(texto):
    return texto.upper()
def en_minusculas(texto):
    return texto.lower()
def saludar(func):
    saludo = func("Hola, ¿que tal?")
    print(saludo)
#============================================
#con strings
#============================================
saludar(en_mayusculas)
saludar(en_minusculas)
#============================================
#funciones abstractas dentro de funciones
#su resultado es otra funcion
#============================================
def divisor(x):
    def dividendo(y):
        return y/x
    return dividendo
#============================================
#primero generamos la funcion y/2
#============================================
division = divisor(2)
#============================================
#la usamos para calcular 3/2
#============================================
print(division(3))
#============================================
#uso de la funcion map con una lista
#============================================

#============================================
#lista de ciudades y su temperatura
#============================================
temps = [("berlin",29),("cairo",36),("buenos aires",19),("Los angeles",26),("Tokyo",27),("Nueva York",28),("londres",22),("pekin",32),("Mexico Tenochtitlan",23)]
C_a_F = lambda datos: (datos[0],(9/5)*datos[1] + 32)
print(list(map(C_a_F, temps)))

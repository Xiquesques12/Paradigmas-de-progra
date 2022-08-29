''' Este es un supercomentario
    de inicio a nuestro resumen
'''
#====================
# Operaciones básicas
#====================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5) #raiz cuadrada
print (10%2)
print (10%0.1) #exlusivo en python

#=========================================
#para saber el tipo de objeto se usa type
#=========================================
t = 0
print (type(t)) #entero
t=3.6
print(type(t)) #real (flotante)
t = True
print(type(t)) #booleano (bool)

#========================
#mensajes a pantalla
#========================

print ("este es un comando de phyton. ", "este es otro enunciado.",t)
print ('id: ', 1)
print ('First Name: ','steve')
print ('last name: ', 'jobs')
print (' vamos a sumar esto' + "con esto otro")

#==============================================
#continuar una instruccion en varios renglones
#==============================================
if 100 > 99 and \
        200 <= 300 and\
        True != False:
            print ('Hello world')

#=============================================
#comandos diferentes en la misma línea
#============================================
print ("Hola "); print ("tu!!")     #se considera mala práctica

#============================================
# Usando paréntesis redondos, cuadros o llaves
#se pueden escribir en varios renglones
#=============================================

list = [1,2,3,4,
        5,6,7,8,
        9,10,11,12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] 
print (list)
print (matriz) 

#================================================================
#Identacion esrticta para procesos dependientes de : (dos puntos)
#=================================================================
if 10>5:
    print ("diez es mayor que cinco")
    print ("otra identación")
for i in list:
    print (i)
    print ("ok")
if 10>5:
    print("verdadero")
    if 10<20:
        print ("verdadero")
elif 5>3: #comienza segundo condicional
    print ("esto no se imprimirá")
else:
    print ("aqui nunca llega")

#===========
#funciones
#===========

def say_hello(name):
    print ("hello ",name)
    print ("welcome to python tutorials")
say_hello("julián")
#====================================================
#imput permite obtener datos del usuario en prompter
#===================================================
nombre = input("dame tu nombre: ")
print("hola como estas", nombre)

#================================================
# los enteros son de precision limitada
#===============================================
y = 500000000000000000000000000000000000
print(y)
#===========================================================
#se pueden delimitar números con guion bajo pero no con coma
#===========================================================
y = 5_000_000
print (y)
#===========================================================
#la funcion int() cambia de strings y floats a enteros
#===========================================================
numero = int(input("dame tu edad: "))
type(numero)

#==================================================
#la notacion cientifica de flotantes utiliza e o E
#===================================================
# 1.2 x 10^{-9}
#===============
y= 1.2E-09
print(y)

#=======================================================
#la funcion float() convierte strings y enteros a floats
#=======================================================
y = float("14.3")
print(y)
#=======================================================
#los complejos se escriben con la raiz de menos uno
#j siempre con un numero como prefijo
#no acepta la j suelta
#=======================================================

z= 1+1j
#suma +
#resta -
# multiplicacion *
#division /
# modulo %
# exponente **
#// funcion piso
#Funciones para tranformar números int() float() complex()
#Operaciones abs() round() pow()

print(round(3.14159 , 4))

#===========================
#strings de varias lineas
#===========================
parrafo = """ En el bosque de la china
la chinita se perdió """
print(parrafo)

#==============================================
#la funcion len() obtiene el tamaño del string
#==============================================
n=len(parrafo)
print(n)

#===========================================================
# las letras en un string ocupan lugares como en un arreglo
#tambien de atras parea adelante comenzando en -1 el ultimo)
#===========================================================
palabra = "hola"
print (palabra[0])
print (palabra[-4])


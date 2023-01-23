#=============================
#una clase para un objeto vacio
#no esta tan vacio, necesita
#la palabra pass= pasar
#=================================
class objetoVacio:
    pass
#==================================
#nada es un ObjetoVacio
#=================================
nada = objetoVacio()
print(type(nada))
#================================
#la clase llanta
#=============================
class Llanta:
    #=============================
    #variable cuenta es de toda la clase
    #==============================
    cuenta= 0
    #================================
    #funcion constructora de identidad
    #_init_ es una funcion reservada
    #comienza con uno mismo : self
    #pero puede ser otro nombre (mi)
    #parametros de entrada = default
    #====================================
    def __init__(mi,radio=50,ancho=30,presion=1.5):
        #variable de la estructura llanta
        Llanta.cuenta += 1
        #variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion
#==================================================
#objetos (instanciados)
#=========================================
llanta1=Llanta(50,30,1.5)
llanta2= Llanta(presion=1.2)
llanta3= Llanta()
llanta4= Llanta(40,30,1.6)
#============================================
#objeto que contiene otros objetos
#========================================
class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1=ll1
        mi.llanta2=ll2
        mi.llanta3=ll3
        mi.llanta4=ll4
micoche= Coche(llanta1,llanta2,llanta3,llanta4)
print('total de llantas', Llanta.cuenta) #variable global de la clase
print('presion de la llanta 4', llanta4.presion) #presion de la llanta 4
print('radio de la llanta 4', llanta4.radio)
print('presion de la llanta 1 de mi coche', micoche.llanta1.presion)
#===========================
#encapsulamiento
#===========================

#======================================================
#uso de la funcion de phyton poperty para poner y obtener atributos
#======================================================
class Estudiante:
    def __init__(mi):
        mi._nombre = ''
    def ponerme_nombre(mi,nombre):
        print('se llamo a ponerme_nombre')
        mi._nombre= nombre
    def obtener_nombre(mi):
        print('se llamo a obtener_nombre')
        return mi._nombre
    nombre=property(obtener_nombre, ponerme_nombre)    
#====================================
#crear objeto estudiantes sin nombre
#=======================================
estudiante = Estudiante()
#========================================
#ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre
#(sin tener que llamar explicitamente a la funcion)
#================================================
estudiante.nombre = 'Diego'
#==============================================
#obtener el nombre con el metodo obtener nombre
#_nombre es una variable encapsulada ( no visible desde afuera)
#(sin tener que llamar explicitamente a la funcion obtemer_nombre)
#====================================================
print(estudiante.nombre)
#esto no funciona
#print(estudiante._nombre)
#==========================================
#Herencia de clases
#=========================================
class Cuadrilatero:
    def __init__(mi,a,b,c,d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d
    def perimetro(mi):
        p=mi.lado1+mi.lado2+mi.lado3+mi.lado4
        print('perimetro',p)
        return p
#============================================
#su hijo rectagulo
#rectangulo es hijo de cuadrilatero
#rectangulo (cuadrilatero)
#=============================================
class  Rectangulo(Cuadrilatero):
    def __init__(self,a,b):
        #constructor de su madre
        super().__init__(a, b, a, b)
#====================================
#su nieto cuadrado
#su hijo de rectangulo
#===================================
class Cuadrado(Rectangulo):
    def __init__(self, a, ):
        super().__init__(a,a)
    def area(self):
        area=self.lado1**2
        return area
    #def perimetro(self):
    #   p=4.0*self.lado1
    #   print('perimetro =',p)
    #   return p
#=============================
#crear un cuadrado
#=============================
Cuadrado1 = Cuadrado(5)
#=======================================
#llamar al metodo perimetro de su abuelo cuadrilatero
#=============================
perimetro1= Cuadrado1.perimetro()
#============================================
#llamar a su propio metodo area
#============================================
area1=Cuadrado1.area()
print('perimetro = ', perimetro1)
print('area = ',area1)
#============================================
#sobre-escribir un metodo de su madre o abuela o tatarabuela...
#es volver a definir una funcion ya existente
#============================================
class A:
    _a:float=0.0
    _b:float=0.0
    _c:float=0.0

    def __init__(self,a:float,b:float,c:float):
        self.a= a
        self.b = b
        self._c= c
#============================================
#la clase B tiene dos numeros reales
#============================================
class B:
    _d:float= 0.0
    _e:float= 0.0
    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e
        #============================================
        #metodo sumar todo (internos + externos)
        #============================================
    def sumar_todo(self,aa:float,bb:float):
        x:float=self.d+self.e+aa+bb
        return x
#============================================
#asociacion
#============================================
#usando objetos independientes
objetoA=A(1.0,2.0,3.0)
objetoB=B(4.9,5.0)
print(objetoB.sumar_todo(objetoA.a,objetoA.b))
#============================================
#El objeto c tiene dos reales y un objeto A
#El objeto A se instancia dentro de C
#============================================
class C:
    _d:float=0.0
    _e:float=0.0
    _Aa=A=None
    def __init__(self,d:float,e:float):
        self.d=d
        self.e=e 
        #A esta instanciado adentro
        self.Aa= A(1.0,2.0,3.0)
    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.b
        return x
#============================================
#composicion
#contiene otro objeto dentro
#============================================
objetoC=C(4.0,5.0)
print(objetoC.sumar_todo())
#============================================
#objeto D tiene dos reales y un objeto A
#defiido por fuera
#============================================
class D:
    _d:float=0.0
    _e:float=0.0
    _Aa:A=None
    def __init__(self,d:float,e:float,Aa:A):
        self.d=d
        self.e=e
        self.Aa=Aa
    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
#============================================
#agregacion
#construye el objeto agregado por fuera
#============================================
objetoD = D(4.0,5.0, objetoA)
print(objetoD.sumar_todo())
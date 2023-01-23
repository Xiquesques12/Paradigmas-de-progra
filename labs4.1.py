#============================================
#clase computadora
#============================================
class computadora:
    marca: str = None
    capacidad: int = 0
    ram: int= 0
    #============================================
    #constructor
    #============================================
    def __init__(self,marca:str, capacidad:int, ram:int):
        print(f"accediendo al constructor de la pc {marca}")
        self.marca=marca
        self.capacidad=capacidad
        self.ram=ram
    def imprimirInfoPC(self):
        print(f"esta es la computadora marca : {self.marca} con almacenamiento de {self.capacidad}GB y memoria de {self.ram}GB")
    #============================================
    #Destructor
    #============================================
    def _del_(self):
        print(f"se elimono la computadora: {self.marca}")
#============================================
#objeto persona
#============================================
class persona:
    nombres:str=None
    apellidos: str=None
    edad: int=0
    direccion: str = None
    computadora= computadora=None
    #============================================
    #Constructor de persona
    #============================================
    def __init__(self,nombres:str,apellidos:str,edad:int, direccion:str, marca:str,capacidad:int,ram:int) -> None:
        self.nombres=nombres
        self.apellidos=apellidos
        self.edad= edad
        self.direccion=direccion
        self.computadora=computadora(marca,capacidad,ram)
        print(f"---Accedimos al constructor de la persona: {nombres}{apellidos}")

    def imprimirInfo(self) -> None:
        print(f"---Mi nombre es {self.nombres}{self.apellidos}, tengo{self.edad}años de edad, vivo en {self.direccion}")
        self.computadora.imprimirInfoPC()
    #============================================
    #destructor
    #============================================
    def __del_(self):
        print(f"---Eliminamos el objeto...{self.nombres}{self.apellidos}")

#============================================
#funcion 1 es el programa
#============================================
def funcion1():
    persona1=persona("carlos","perez",40,"xochimilco","lenovo",700,8)
    print("\n")
    persona1.imprimirInfo()
    print("\n")
    persona2=persona("magdalena","carrillo",35,"jalapa","IBM",200,4)
    print("\n")
    persona2.imprimirInfo()
    print("\n")
#============================================
#llamar funcion1
#============================================
funcion1()

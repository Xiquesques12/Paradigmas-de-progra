from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario
#============================================
#para llenar la interface hay que heredar la clase
#============================================
class BaseDeDatos(RepositorioDeUsuarios):
    _host:str
    _user:str
    _password:str

    def __init__(mi,host:str,user:str,password:str):
        mi._host=host
        mi._user=user
        mi._password=password
    def abrir(mi) -> None:
        print(f"Abriendo la conexion a la Base de datos: {mi._host}:{mi._user}:{mi._password}")
    def guardar(mi,usuario:Usuario) -> None:
        userElements = {"nombre":usuario.getNombre(),"apellido":usuario.getApellido(),"edad":usuario.getEdad()}
        print(f"Guardandoel usuario en la base de datos {usuario.getNombre()}\n")
        print(f"INSERTAR DATOS DEL USUARIO ('{userElements['nombre']}','{userElements['apellido']}',{userElements['edad']})")

    def cerrar(mi) -> None:
        print("cerrando la conexion")
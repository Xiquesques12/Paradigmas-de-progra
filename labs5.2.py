from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#============================================
#S3 es hijo de RepositorioDeUsuarios
#============================================
class S3(RepositorioDeUsuarios):
    _clientId: str
    _secretKey: str
    _bucket:str
    def __init__(mi,clientId:str,secretKey:str,bucket:str):
        mi._clientId= clientId
        mi._secretKey=secretKey
        mi._bucket=bucket
    def abrir(mi) -> None:
        print(f"Estableciendo conexion a AWS S3 {mi._clientId}:{mi._secretKey}")
    def guardar(mi,usuario:Usuario) -> None:
        userData ={"nombre": usuario.getNombre(),"apellido":usuario.getApellido(),"edad":usuario.getEdad()}
        print(f"guardando usuario de la bandeja: {mi._bucket}:{userData}")
    def cerrar(mi) -> None:
        print("cerrando conexion AWS S3")
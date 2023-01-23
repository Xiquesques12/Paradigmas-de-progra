from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario 
#============================================
#implementa la interface repositorioDeUsuarios
#============================================

class SistemaDeArchivos(repositorioDeUsuarios):
    _directorio: str
    def __init__(mi, directorio:str):
        mi._directorio=directorio
    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi._directorio}")
    def guardar(mi,usuario:Usuario) -> None:
        xml=f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad}</age></roor>"
        print(f"Guardando usuario en el archivo :{mi,_directorio}/{usuario.getNombre()}")
        print(xml)

        def cerrar(mi) -> None:
            print("cerrando el archivo")
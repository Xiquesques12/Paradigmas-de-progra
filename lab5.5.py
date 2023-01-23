from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
#============================================
#clase storemanager
#NO Tiene variables!!
#============================================
class ManejoDeInscripciones:
    #============================================
    #Decorador staticmenthod
    #el objeto solo tiene la funcion de inscribir usuario
    #Envuelve la funcion sin llamar variables locales
    #el objeto ManejoDeInscripciones es la interfaceintercambiable
    #============================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios:RepositorioDeUsuarios) -> None:
        print("-------> Guardando usuario...\n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar()
        repositorioDeUsuarios.cerrar()
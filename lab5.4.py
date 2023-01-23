from aplicacion.modelos.usuario import Usuario
#============================================
#este objeto es una interface
#============================================

class RepositorioDeUsuarios:
    def abrir(mi) -> None:
        pass
    def guardar(mi,usuario:Usuario) -> None:
        pass
    def cerrar(mi) -> None:
        pass